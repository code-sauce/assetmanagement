import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import re


def _get_total_matches(re_ex, content):
	match_count = 0
	for match in re_ex.finditer(content):
		match_count += 1
	return match_count


def flatten_animations():
	#re_ex = re.compile(r"\<animation.+?\>")
	re_ex = re.compile(r"(\<animation.+?\>)([\s\S]+?)(\<\/animation\>?)")
	f = open(os.path.join(dir_path, '../', 'static/animations/Boxing-orig.dae'))
	xml_content = f.read()
	f.close()
	first_animation_tag_index = xml_content.find("<animation ")
	last_animation_tag_index = xml_content.rfind("</animation>") + len("</animation>")
	pre_animation_content = xml_content[:first_animation_tag_index]
	post_animation_content = xml_content[last_animation_tag_index:]
	reex_search_string = xml_content[first_animation_tag_index:last_animation_tag_index]
	f = open('foo', 'w')
	f.write(reex_search_string)
	f.close()
	match_count = _get_total_matches(re_ex, reex_search_string)

	matches = re_ex.finditer(reex_search_string)

	match_number = 0
	edited_content = ""
	for match in matches:
		if match_number == 0:
			# for the first group, we want the opening <animation> tag, not the closing one
			edited_content += match.group(1)
			edited_content += match.group(2)
		elif match_number >= match_count - 1:
			# for the last group, we want the ending </animation> tag
			print("last tag.... adding </animation> tag")
			edited_content += match.group(2)
			edited_content += match.group(3)
		else:
			# we don't want any of the opening or closing <animation> tag in the middle animations
			edited_content += match.group(2)
		match_number += 1 
	edited_content = pre_animation_content + edited_content + post_animation_content
	f = open('.edited.xml', 'w')
	f.write(edited_content)
	f.close()
	import pdb; pdb.set_trace()
if __name__ == '__main__':
    flatten_animations()
