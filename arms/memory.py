import psutil,os
import platform,winsound
def memory_details():
    memory = psutil.virtual_memory()
    total = memory.total
    available = memory.available
    used = memory.used
    percent = memory.percent
    
   

    return (f"Total memory: {total/(1024**2):.2f} MB\n"
            f"Available memory: {available/(1024**2):.2f} MB\n"
            f"Used memory: {used/(1024**2):.2f} MB\n"
            f"Percentage of memory in use: {percent}%\n"
            
           )



def cpu_details():
    cpu_count = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent()
    cpu_freq = psutil.cpu_freq()
    cpu_stats = psutil.cpu_stats()
    cpu_times = psutil.cpu_times()
    return (f"Number of CPUs: {cpu_count}\n"
            f"CPU usage: {cpu_percent}%\n"
            f"Current frequency: {cpu_freq.current:.2f} MHz\n"
            f"Min frequency: {cpu_freq.min:.2f} MHz\n"
            f"Max frequency: {cpu_freq.max:.2f} MHz\n"
            f"Number of context switches: {cpu_stats.ctx_switches}\n"
            f"Number of interrupts: {cpu_stats.interrupts}\n"
            f"Number of soft interrupts: {cpu_stats.soft_interrupts}\n"
            f"Number of system calls: {cpu_stats.syscalls}\n"
    )

def system_info():
    print("System:", platform.system())
    print("Node Name:", platform.node())
    print("Release:", platform.release())
    print("Version:", platform.version())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())

def check_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged

    if percent <= 20 and not plugged:
        winsound.PlaySound('abc',winsound.SND_LOOP)
        print(f"please charge you battery is {percent} it need rest")
    else:
        print(f"you are good to go with {percent}% of battery")
        




