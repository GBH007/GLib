# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

start_template='''
<html><head>
<style type="text/css">
{css}
</style>
<title>Report</title>
</head><body>
'''
end_template='''</body></html>'''
css_template='''
.table{
	border: 2px solid black;
	text-align: center;
}
tr:hover{
	background-color: yellow;
}
.selected{
	border: 2px solid red;
	background-color: red;
}
.r0{
	background-color: #BFBFBF;
}
.r1{
	background-color: white;
}
.None{
}
.text{
}
'''
