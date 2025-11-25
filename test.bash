#!/bin/bash 
# SPDX-FileCopyrightText: 2025 Satoh-Narumi
# SPDX-License-Identifier: BSD-3-Clause

ng () {
	echo ${1}行目ダメよ
	res=1
}

res=0

mkdir -p test_sys/src
touch test_sys/src/copu.txt
touch test_sys/src/movu.txt
cd test_sys

normal_output_copy = "'src/copu.txt'"
normal_output_move = "'src/movu.txt'"
out_copy=$( ../fetch -c test_sys/src copu.txt)
out_move=$( ../fetch -m test_sys/src movu.txt)
exit_code=$?

[ "${out_copy}" = "${normal_output_copy}" ] || ng "$LINENO"
[ "${out_move}" = "${normal_output_move}" ] || ng "$LINENO"

[ '-f ./copu.txt' ] || ng "$LINENO"
[ '-f./movu.txt' ] || ng "$LINENO"
[ ${exit_code} -eq 0 ] || ng "$LINENO"

#以下ダメ
out_1=$( ../fetch src/copu.txt)
out_2=$( ../fetch -m movu.txt)
exit_code=$?

[ "${out_1}" = "${normal_output_copy}" ] || ng "$LINENO"
[ "${out_2}" = "${normal_output_move}" ] || ng "$LINENO"

[ '-f ./copu.txt' ] || ng "$LINENO"
[ '-f ./movu.txt' ] || ng "$LINENO"
[ ${exit_code} -eq 2 ] || ng "$LINENO"

cd ..
rm -rf test_sys

[ "${res}" = 0 ] && echo OK
exit $res
