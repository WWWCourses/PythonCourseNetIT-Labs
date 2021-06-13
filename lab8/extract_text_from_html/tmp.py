import re


def strip_all_tags(html):
	rx = re.compile(r'(?s)<.+?>')
	return rx.sub('',html)

def strip_mult_spaces(data,count):
	rx = re.compile(r'\s{'+str(count)+',}')
	print(rx)
	return rx.sub('',data)

def print_all_tags(html):
	rx = re.compile(r'(?s)<.+?>')
	tags = rx.findall(html)

	print(len(res))
	for r in res:
		print(r)

def extrac_info(html):
	rx = re.compile(r'(?is)<div class="ac-head">.+<span>\s+(\d+)\s*<\/span>\s*<div>(.+?)<\/div>')
	res = rx.findall(html)
	print(res[0][1])


html = '''<div class="ac-head">
												<button class="btn btn-link" data-toggle="collapse" data-target="#collapse2"
												aria-expanded="true" aria-controls="collapse2">
													<span>
                                          02                                       </span>
                                       <div>Променливи в Питон. (семестър 1)  (12.03.2020 в 18:30 ч.)</div>
                                       <div style="font-size:14px;">Модул: Основи на Питон, Продължителност: <b>3 учебни часа</b></div>
												</button>
											</div>
'''

extrac_info(html)

# data = strip_all_tags(html)
# print(data)

# data_cleaned=strip_mult_spaces(data,3)
# print(data_cleaned)






'''References:
		https://docs.python.org/3/library/re.html#re.sub
'''




