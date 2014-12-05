
---

* 1. HTML中调用js/python/ruby

``` html
<html>
 <head>
  <script type="text/javascript">
	function functionOne() { alert('You clicked the top text'); }
	function functionTwo() { alert('You clicked the bottom text'); }
  </script>
  <script type="text/javascript" src="j1.js"></script>
 </head>
<body>

 <!-- js in html -->
 <p><a href="#" onClick="functionOne();">Top Text</a></p>
 <p><a href="javascript:functionTwo();">Bottom Text</a></p>
 <!--js inline in the html -->
 <p><a href="#" onClick="alert('Hello');">Click Me</a></p>
 
 </body>
</html>
```
