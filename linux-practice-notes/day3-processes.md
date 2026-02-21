# Processes & System Monitoring

## Date Completed
20 February

## Commands Practiced

### Process Management
- ps aux - Listed all running processes
- top - Monitored system in real-time (press q to exit)
- ps aux | grep python - Searched for specific processes
- ps aux | grep code - Found code-related processes

### System Resources
- df -h - Checked disk space usage
- free -h - Checked memory (RAM) usage
- whoami - Displayed current username
- uptime - Showed system uptime and load average
- uname -a - Displayed system information

## Key Learnings

- Processes are running programs with unique PIDs (Process IDs)
- Can monitor CPU and memory usage with ps and top
- Pipes (|) send output from one command to another
- grep filters/searches command output
- Disk space and memory are important to monitor
- Load average shows how busy the system is

## Example Output

### Disk Usage
Filesystem Size Used Avail Use% /dev/sda1 50G 20G 28G 42%

### Memory Usage
         total        used        free
Mem: 15Gi 8.0Gi 3.5Gi

### Process Count
Total processes running: ~340

## Practice Notes

Learned how to find resource-intensive processes and monitor system health. Understanding that lower load average = better performance. Disk at 42% usage is healthy. The pipe operator (|) is powerful for combining commands.
