def main():
    print 'Running reboot script...'

    from datetime import datetime
    with open('/home/pi/cron_scripts/reboot.log', 'a') as f:
        timeStr = str(datetime.now())
        print 'Output: ', timeStr
        f.write(timeStr + '\n')

    print 'End reboot script...'



if __name__ == '__main__':
    main()
