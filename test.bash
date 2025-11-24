#!/bin/bash 
# SPDX-FileCopyrightText: 2025 Satoh-Narumi
# SPDX-License-Identifier: BSD-3-Clause

ng () {
	echo ${1}行目ダメよ
	res=1
}

res=0

### NORMAL INPUT ###
out=$(seq 5 | ./fetch)
[ "${out}" = 15 ] || ng "$LINENO"


## STRANGE INPUT ###
out=$(echo あ | ./fetch)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(echo  | ./fetch)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

[ "${res}" = 0 ] && echo OK

exit $res
