# timetrack


Track your time easily with an usb stick.



### Requirements

- pamusb
- Python 3
- libnotify



### Installation

- Clone this repository anywhere you want
- Run the installation script
  It will copy everything into its right place
  and removes the git-repository.
- Change the `NAME` in `/opt/Timetrack/src/timetrack.py`
- Install and configure pamusb and set the lock and unlock
  function in your config file like that
  - lock: `/opt/timetrack/src/timetrackctl.py stop`
  - unlock: `/opt/timetrack/src/timetrackctl.py start`



### Usage

- Start the daemon with
  `sudo systemctl start timetrack.service`
- *Optional:* Enable the timetrack-service at boot with
  `sudo systemctl enable timetrack.service`
- Stick in the usb-stick to start the work time and remove it
  to stop the work time.
- Alternatively you are able to start and stop the work time 
  over the command line with
  `/opt/timetrack/src/timetrackctl.py start/stop`



### Evaluate your data

In order to evaluate your saved data just run

`/opt/timetrack/src/timetrackctl.py evaluate`

It will create an HTML-document in `~/Timetrack/`, which 
displays your data in a table.



### TODO

- Better visualization
- Code refactoring
- Better documentation
- Testing



### License 

(c) 2016 - Daniel Jankowski


Licensed under the GNU Lesser General Public License Version 3 (LGPLv3).
See [LICENSE](./LICENSE) for more details.
