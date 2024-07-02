#!/usr/bin/env python3




def report_time( prefix: str, start_time: int, end_time: int, report_time: bool =False):

    total_time = end_time - start_time
    
    reported_time = total_time
    uom = "seconds"

    if total_time > 60:
        uom = "minutes"
        reported_time = total_time / 60
    
    if report_time:
        print(prefix, {str(round(reported_time, 2))}, uom)



