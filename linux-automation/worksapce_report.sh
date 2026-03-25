#!/bin/bash
echo "=== Workspace Daily Report ==="
echo "Date: $(date)"
echo "System Status:"
df -h | grep '^/dev/'
echo "Current Users:"
who
echo "Active Processes:"
ps aux | wc -l
echo "Memory Usage:"
free -h
echo "Report generated at: $(date +%H:%M:%S)" 
