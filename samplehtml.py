import webbrowser

temp=open('sample1.html','w')

code="""
<html>
<body> <h1>Welcome to Vcode!!!1</h1>
<h2> hello</h2>
</html>
"""

temp.write(code)
temp.close()

webbrowser.open_new_tab('sample1.html')

