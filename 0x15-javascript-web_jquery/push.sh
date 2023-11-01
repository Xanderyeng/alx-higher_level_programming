#!/bin/bash

make_js_files_executable() {
	for file in $(find . -type f -name "*.js"); do
		chmod +x "$file"
	done
}

make_js_files_executable

git add .
git commit -m "$1"
git push
