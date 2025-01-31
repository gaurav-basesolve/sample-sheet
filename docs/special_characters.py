"module with a list of special characters"
import typing as t
# Special characters encounter in sample sheet
special_characters_string: str = "À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö × Ø Ù Ú Û Ü Ý Þ ß à á â ã ä å æ ç è é ê ë ì í î ï ð ñ ò ó ô õ ö ÷ ø ù ú û ü ý þ ÿ"
special_characters_list: t.List[str] = list(set(special_characters_string))
special_characters_list.remove(" ")
special_characters_string: str = ("").join(special_characters_list)

