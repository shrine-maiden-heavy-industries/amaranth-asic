#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause

from setuptools import setup, find_packages
from pathlib    import Path

REPO_ROOT         = Path(__file__).parent
README_FILE       = (REPO_ROOT / 'README.md')
REQUIREMENTS_FILE = (REPO_ROOT / 'requirements.txt')

def vcs_ver():
	def scheme(version):
		if version.tag and not version.distance:
			return version.format_with("")
		else:
			return version.format_choice("+{node}", "+{node}.dirty")
	return {
		"relative_to": __file__,
		"version_scheme": "guess-next-dev",
		"local_scheme": scheme
	}

def doc_ver():
	try:
		from setuptools_scm.git import parse as parse_git
	except ImportError:
		return ""

	git = parse_git(".")
	if not git:
		return ""
	elif git.exact:
		return git.format_with("{tag}")
	else:
		return "latest"

setup(
	name = 'Amaranth-ASIC',
	use_scm_version  = vcs_ver(),
	author           = 'Shrine Maiden Heavy Industries',
	author_email     = 'nya@catgirl.link',
	description      = 'An amaranth-lang toolkit for ASIC flows',
	license          = 'BSD-3-Clause',
	python_requires  = '~=3.8',
	zip_safe         = True,
	url              = 'https://github.com/shrine-maiden-heavy-industries/amaranth-asic',

	long_description = README_FILE.read_text(),
	long_description_content_type = 'text/markdown',

	setup_requires   = [
		'wheel',
		'setuptools',
		'setuptools_scm'
	],

	install_requires  = REQUIREMENTS_FILE.read_text().splitlines(),
	packages          = find_packages(
		where = '.'
	),
	package_data      = {},

	extras_require    = {},
	entry_points      = {
		'console_scripts': [

		],
	},

	classifiers       = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Topic :: Software Development',
		'Topic :: System :: Hardware',
	],

	project_urls      = {
		'Documentation': 'https://github.com/shrine-maiden-heavy-industries/amaranth-asic',
		'Source Code'  : 'https://github.com/shrine-maiden-heavy-industries/amaranth-asic',
		'Bug Tracker'  : 'https://github.com/shrine-maiden-heavy-industries/amaranth-asic/issues',
	}
)
