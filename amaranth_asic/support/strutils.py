# SPDX-License-Identifier: BSD-3-Clause
import textwrap
import re
from typing     import Any

from markupsafe import Markup

__doc__ = '''\

'''

__all__ = (
	'ascii_escape',
	'tcl_escape',
	'tcl_quote',

)

def ascii_escape(string: str) -> str:
	def escape_match(match: re.Match) -> str:
		if match.group(1) is None:
			return
		else:
			return f'_{ord(match.group(1)[0]):02x}_'

	return ''.join(map(escape_match, re.finditer(r'([^A-Za-z0-9_])|(.)', string)))

def tcl_escape(string: Any) -> str:
	if isinstance(string, Markup):
		return string
	else:
		string = str(string)

	return '{' + re.sub(r"([{}\\])", r"\\\1", string) + '}'

def tcl_quote(string: Any) -> str:
	if isinstance(string, Markup):
		return string
	else:
		string = str(string)

	return '"' + re.sub(r"([$[\\]])", r"\\\1", string) + '"'
