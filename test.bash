#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Satoh-Narumi
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"
ng () {
	echo ${1}行目ダメよ
	res=1
}
res=0

out=$(echo testing an input test | ./adfg)
[ "${out}" = "GD_AV_GA_GD_DF_FD_DA_AA_FD_DF_FD_FG_GF_GD_GD_AV_GA_GD" ] || ng "$LINENO"

out=$(echo GD_AV_GA_GD_DF_FD_DA_AA_FD_DF_FD_FG_GF_GD_GD_AV_GA_GD | ./adfg)
[ "${out}" = "testinganinputtest" ] || ng "$LINENO"



out=$(echo てすちんぐ　あん　いんぷと　てすと | ./adfg)
[ "${out}" = "Wrong Input." ] || ng "$LINENO"

out=$(echo  | ./adfg)
[ "${out}" = "Wrong Input." ] || ng "$LINENO"

[ "${res}" = 0 ] && echo OK

exit $res