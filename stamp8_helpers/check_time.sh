#!/bin/bash



check_time() {

    
    local x="[check_time]: "

    start_time=$1
    end_time=$2
    uom="seconds"
    total_time=$((${end_time} - ${start_time}))
    report_time=${total_time}
    if (($total_time>60)); then
        uom="minutes"
        report_time=$(($total_time / 60))
        echo "The Bash Task took ${report_time} ${uom} to complete"
        # exit 0
    else
        echo "The Bash Task took ${report_time} ${uom} to complete"
        # exit 0
    fi






}