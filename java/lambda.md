

如果{}中只有一句代码，可以省略{}  
return FuturUtil.supply((userId) -> { return xxservice.query(userId)});  
return FuturUtil.supply((userId) -> xxservice.query(userId));
