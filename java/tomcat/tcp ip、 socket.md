### tcp_nodelay  
  true时，小的数据包直接发送  
  false时，发送端等待一段时间，将小的数据包封装成大一点的数据包,提高网络利用率

### 统计各种状态的连接数  
  NF当前行的列数， netstat参数必须为an  
  netstat -an | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'
