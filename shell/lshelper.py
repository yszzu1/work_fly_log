#!/usr/bin/python
# -*- coding:utf-8 -*-

#注意：      不能使用print等语句在标准输出中随意打印字符串      :注意#

#注意：  要保证LsHelper.py文件在标准输出中输出合法的json字符串  :注意#

import httplib
import sys
import json
import os
import time
from time import sleep
import logging
import subprocess
import base64
import hmac,hashlib
import re

server = "127.0.0.1"
port = 5180
SLEEPTIME = 3
CHECKTIMES = 30
TIME_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
date = time.strftime(TIME_FORMAT, time.gmtime())
LOGPATH = '/var/log/'
logfileprefix = 'LsHelper.py_'
LOGFMT = '%(asctime)s-%(name)s-%(filename)s:%(lineno)s-%(message)s'

#the log level can be set to: logging.DEBUG logging.INFO logging.WARNING logging.ERROR logging.CRITICAL
LOGLEVEL = logging.WARNING
LOGDATEFMT = '%a, %d %b %Y %H:%M:%S'

logging.basicConfig(level = LOGLEVEL,
                    format = LOGFMT,
                    datefmt = LOGDATEFMT,
                    filename = (LOGPATH + logfileprefix + time.strftime("%Y-%m-%d")+".log"),
                    filemode = 'a')
lgr = logging.getLogger("PID:%s"%(os.getpid()))

def isJSONValid(jsonArg):
    if not jsonArg:
        print '{"errCode":9994,"unifiedErrCode":1343225644,"infos":"Invalid argv: %s, json argument is a must but provided None"}' % (sys.argv)
        lgr.error("Invalid argv: %s, json argument is a must but provided None" % (sys.argv))
        sys.exit(1)

def isParamValid(ParamReg, param):
    match = re.match(ParamReg, param)
    if not match:
        print '{"errCode":9995,"unifiedErrCode":1343225645,"infos":"Invalid argv: %s, the id does not match our regular expression"}' % (sys.argv)
        lgr.error("Invalid argv: %s, the id does not match our regular expression" % (sys.argv))
        sys.exit(1)

def isAPIValid(param, ParamRange = []):
    if param not in ParamRange:
        print '{"errCode":9996,"unifiedErrCode":1343225646,"infos":"Invalid argv: %s, the api does not exist"}' % (sys.argv)
        lgr.error("Invalid argv: %s, the api does not exist" % (sys.argv))
        sys.exit(1)

def isArgvValid(n):
    if len(sys.argv) < n:
        print '{"errCode":9997,"unifiedErrCode":1343225647,"infos":"Invalid argv: %s, no enough args provided"}' % (sys.argv)
        lgr.error("Invalid argv: %s, no enough args provided" % (sys.argv))
        sys.exit(1)

def getRelatedJars():
    targets = ["tracelogger", "obs_util", "upfAdapter", "obs_config", "obs_memcache_client", "commons-lang", "commons-collections", "commons-configuration", "commons-logging", "commons-codec", "log4j", "servlet-api", "httpclient", "httpcore", "httpmime", "bcpkix-jdk15on", "jettison", "xmlsec", "authentication", "java_memcached-release","commons-pool", "commons-dbcp", "spring-tx", "spring-core", "spring-jdbc", "jackson-all", "activemq-all", "spring-beans", "bcprov-jdk15on", "protobuf-java", "dom4j", "gsjdbc4", "commons-beanutils", "aopalliance", "spring-aop"]
    path = "/opt/uds/lib/common/"
    jars = os.listdir(path)
    targets.sort()
    jars.sort()
    result = ""
    for jar in jars:
        for target in targets:
            n = len(target)
            if jar[0:n] == target:
                result = result + path + jar + ":"
                targets.remove(target)
                break;
    return result[:-1]

def getAdminInfo(param = 'GetAdminInfo'):
    try:
        mainClass = "com.huawei.uds.auth.gensignature.util.GenSignatureUtil"
        javaArg = "java -cp " + getRelatedJars() + " " + mainClass + " " + param + "> /dev/null"
        lgr.debug("javaArg: %s"%(javaArg))
        p = subprocess.Popen(javaArg, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        returncode = p.poll()
        count = 0
        while returncode == None:
            if count == CHECKTIMES:
                lgr.error('the subprocess to run java command does not terminate in %s seconds...'%(SLEEPTIME * CHECKTIMES))
                p.kill()
                print '{"errCode":9998,"unifiedErrCode":1343225648,"infos":"get admin info failed."}'
                sys.exit(1)
            sleep(SLEEPTIME)
            returncode = p.poll()
            lgr.debug('the %sth time to check java result, returncode:%s, count:%s'%(count, returncode, count))
            count = count + 1
        (stdout_re, stderr_re) = p.communicate()
        if returncode == 0 and stderr_re.count(":") == 1:
            lgr.debug('get java result with %s seconds.'%(SLEEPTIME * count))
            lgr.info(stderr_re[:-1])
            print stderr_re[:-1]
            sys.exit(0)
        else:
            lgr.error("fail to run:%s, please check the arguments."%(javaArg))
            lgr.error("stdout:%s, stderr:%s, returncode:%s"%(stdout_re, stderr_re, returncode))
            print '{"errCode":9998,"unifiedErrCode":1343225648,"infos":"get admin info failed."}'
            sys.exit(1)
        p.kill()
    except Exception, e:
        lgr.error("exception:%s occurs when try to run:%s, please check."%(e, javaArg))
        print '{"errCode":9998,"unifiedErrCode":1343225648,"infos":"get admin info failed."}'
        sys.exit(1)

def checkAdminInfo():
    type = sys.argv[5]
    status = sys.argv[6]
    connection = getConnection()
    path = "/LS/task/?type=" + type + "&status=" + status
    method = "GET"
    httpResponse = getResponse(connection, path, method, isSignChecked = True)
    if httpResponse.status == 200:
        print '{"errCode":0,"unifiedErrCode":1344270336, "infos":"Check admin aksk succeed."}'
        sys.exit(0)
    else:
        print '{"errCode":9992,"unifiedErrCode":1343225649, "infos":"Check admin aksk fail."}'
        sys.exit(httpResponse.status)

def getSignTargetString(uri, method="GET"):
        if "?" in uri:
            uri = uri[:uri.index("?")]
        signTargetstring = "%s\n\n" % method
        signTargetstring += "%s\n" % ("application/json")
        signTargetstring += "%s\n" % (date)
        signTargetstring += "%s" % uri
        return signTargetstring

def getSignResult(uri, method='GET', localSign = True):
    if localSign:
        ak = sys.argv[3]
        sk = sys.argv[4]
        signTargetstring = getSignTargetString(uri, method)
        sign = base64.encodestring(hmac.new(sk, signTargetstring, hashlib.sha1).digest()).strip()
        temp = 'aws ' + ak + ':' + sign
        lgr.info("the sign result : %s"%(temp))
        return temp
    else:
        lgr.info("does not calculate sign result")
        return "-1"

def getConnection():
    try:
        connection = httplib.HTTPConnection(server, port, timeout=10)
        if not connection:
            print '{"errCode":9999,"unifiedErrCode":1343225650,"infos":"Can not connect to %s:%s"}' % (server, port)
            sys.exit(1)
        return connection
    except:
        print '{"errCode":9999,"unifiedErrCode":1343225650,"infos":"Can not connect to %s:%s"}' % (server, port)
        lgr.error("Can not connect to %s:%s" % (server, port))
        sys.exit(1)

def getResponse(connection, path, method, jsonArg = "{}", isSignChecked = True):
    reqheaders = {"Content-type": "application/json", "Accept": "application/json"}
    try:
        if isSignChecked:
            sign = getSignResult(path, method)
            #if sign is calculated correctly, put it into request headers
            if sign != "-1":
                reqheaders['date'] = date
                reqheaders['Authorization'] = sign
            else:
                #if invoke LS's task interface, the sign is a must
                if path.count("task") != 0:
                    lgr.error("failed to calculate sign result, exit of invoking LS's task interface")
                    sys.exit(1)

        if jsonArg != "{}":
            connection.request(method, path, jsonArg, headers = reqheaders)
        else:
            connection.request(method, path, headers = reqheaders)
        httpResponse = connection.getresponse()
        return httpResponse
    except:
        print '{"errCode":9999,"unifiedErrCode":1343225650,"infos":"Can not get response from %s:%s"}' % (server, port)
        lgr.error("Can not getresponse from %s:%s with %s" % (path, method, reqheaders))
        sys.exit(1)

def processResponse(httpResponse):
    if httpResponse.status == 200:
        result = httpResponse.read()
        #the result printed to stdout and to be feteched by CM plugin code
        print result
        lgr.info(result)
        sys.exit(0)
    elif httpResponse.status == 401:
        print '{"errCode":%d,"unifiedErrCode":1343225654,"infos":"%s"}' % (httpResponse.status, "Authentication fails.")
        lgr.error("the httpResponse.status from LS is not 200, status:%s, reason:%s" % (httpResponse.status, httpResponse.reason))
        sys.exit(httpResponse.status)
    else:
        print '{"errCode":%d,"unifiedErrCode":1343225653,"infos":"%s"}' % (httpResponse.status, "The returned result of the HTTP request is abnormal.")
        lgr.error("the httpResponse.status from LS is not 200, status:%s, reason:%s" % (httpResponse.status, httpResponse.reason))
        sys.exit(httpResponse.status)

def listClusterGroup():
    connection = getConnection()
    path = "/LS/clusterGroup"
    method = "GET"
    httpResponse = getResponse(connection, path, method)
    processResponse(httpResponse)

def getClusterGroupById():
    connection = getConnection()
    isArgvValid(6)
    CGId = sys.argv[5]
    CGIdReg = "^[a-zA-Z][a-zA-Z0-9]{0,29}$|^[a-zA-Z][a-zA-Z0-9_-]{1,28}[a-zA-Z0-9]{1,1}$"
    isParamValid(CGIdReg, CGId)
    path = "/LS/clusterGroup/" + CGId
    method = "GET"
    httpResponse = getResponse(connection, path, method)
    processResponse(httpResponse)

def addClusterGroup():
    isArgvValid(6)
    jsonArg = sys.argv[5]
    isJSONValid(jsonArg)
    connection = getConnection()
    path = "/LS/clusterGroup"
    method = "PUT"
    httpResponse = getResponse(connection, path, method, jsonArg)
    processResponse(httpResponse)

def deleteClusterGroupById():
    connection = getConnection()
    isArgvValid(6)
    cgId = sys.argv[5]
    CGIdReg = "^[a-zA-Z][a-zA-Z0-9]{0,29}$|^[a-zA-Z][a-zA-Z0-9_-]{1,28}[a-zA-Z0-9]{1,1}$"
    isParamValid(CGIdReg, cgId)
    path = "/LS/clusterGroup/" + cgId
    method = "DELETE"
    httpResponse = getResponse(connection, path, method)
    processResponse(httpResponse)

def addTask():
    isArgvValid(6)
    jsonArg = sys.argv[5]
    isJSONValid(jsonArg)
    connection = getConnection()
    path = "/LS/task"
    method = "PUT"
    httpResponse = getResponse(connection, path, method, jsonArg, isSignChecked = True)
    processResponse(httpResponse)

APIMAP = {
    "ADMIN":
        {
            "GET":     getAdminInfo,
            "CHECK":   checkAdminInfo
        },
    "CG":
        {
            "LIST":    listClusterGroup,
            "GET":     getClusterGroupById,
            "PUT":     addClusterGroup,
            "POST":    modifyClusterGroupById,
            "DELETE":  deleteClusterGroupById,
            "ENABLE":  enableClusterGroupById
        },
    "REGION":
        {
            "LIST":    listRegion,
            "PUT":     addRegion,
            "ENABLE":  enableRegion,
            "DELETE":  deleteRegionById,
            "POST":    modifyRegionById
        },
}

if __name__ == '__main__':
    isArgvValid(3)
    object = sys.argv[1]
    allObjects = APIMAP.keys()
    isAPIValid(object, allObjects)
    method = sys.argv[2]
    allMethods = APIMAP[object].keys()
    isAPIValid(method, allMethods)

    if object != 'ADMIN':
        isArgvValid(5)

    try:
        pfun = APIMAP[object][method]
        lgr.info("the method called now is %s"%(pfun))
        pfun()
    except Exception, e:
        lgr.error("Exception occurs: %s, argv: %s" % (e, sys.argv))
        print '{"errCode":9993,"unifiedErrCode":1343225651,"infos":"Exception occurs: %s, argv: %s"}' % (e, sys.argv)
        sys.exit(1)
