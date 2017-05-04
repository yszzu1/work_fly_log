
```
<!DOCTYPE HTML>
<html lang="en-US">
<head>
	<meta charset="UTF-8">
	<title></title>
	<link rel="stylesheet" href="../lib/jbox/Skins/Default/jbox.css"/>
	<script type="text/javascript" src="../lib/jquery-1.8.3.js"></script>
	<script type="text/javascript" src="../lib/jbox/jquery.jBox-2.3.min.js"></script>
	
	<script type="text/javascript">
		$(function(){
			//$.jBox.info("xxx");
			//$.jBox.messager("aaaaaaaa");
			
			console.log($.jBox.tipDefaults)
			$.jBox.tip("<span>timeout默认值为3000，当为0时不会自动关闭</span>", 'loading',{timeout: 0});
			 
			$('#btn').click(function(){
				alert("$.jBox.tip模态框会阻塞这个事件的触发");
			});
		})
	</script>
</head>
<body>
	<span>this is html body</span>
	<input type="button" id="btn" value='提示'/>
</body>
</html>
```

http://www.5imvc.com/scripts/jbox/jbox-demo.html
