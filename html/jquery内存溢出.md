

```
$("body").on("click", ".xxxxclass", function () { 
    var aprama = $(this).parent().parent().find(".xxxclass").html();
    $.ajax({
        type: "POST",
        method: "POST",
        url: "/platform/xxx.json",
        data: {"uuid": aprama}  
    }).done(function (msg) {
        alert("Data Saved: " + msg);
    });
})
```

**注意**  
这个aprama不能是jquery对象, 否则会引起ajax内存溢出（变更循环引用）. 上面的.html()不能少
