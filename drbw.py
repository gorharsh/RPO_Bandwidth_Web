"""
This program Calculate Bandwidth Required
 for Given RPO, Data Size and change rate.
"""
import datetime
data = float(input("Please Enter VM / Disk Size in GB: "))
change_rate = float(input("Enter Change rate Between RPO in (%): "))
rpo = float(input("Please Enter Desired RPO in (Min) : "))

change_GB = (data*change_rate)/100
change_rate_Mb = change_GB*8*1000
rpo_sec=rpo*60

bw=change_rate_Mb/rpo_sec
first_rep_time_sec = (data*8*1000)/bw
first_rep_time=datetime.timedelta(seconds=first_rep_time_sec)



print(f"Data Change between RPO: {round(change_GB,2)} GB")
print(f"Bandwidth Required to achieve RPO: {round(bw,2)} Mbps")
print(f"Time for First Replication via above bandwidth : {first_rep_time} HH:MM:SS")