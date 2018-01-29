# task_errata_report
Create a report with all tasks related the errata installation

## Usage
```
 ./task_errata_report.py  -h
usage: task_errata_report.py [-h] -n SERVER -u USERNAME [-p PASSWORD] [-j]
　
Task and job errata report
　
optional arguments:
  -h, --help            show this help message and exit
  -n SERVER, --server SERVER
                        Satellite server (defaults to localhost)
  -u USERNAME, --username USERNAME
                        Username to access Satellite
  -p PASSWORD, --password PASSWORD
                        Password to access Satellite. The user will be asked
                        interactively if password is not provided.
  -j, --job             Use this flag if you want see the jobsa
```
## Output
```
Hostname;TaskAction;TaskID;Username;TaskEnd;TaskResult;TaskState;Errata
test.domain.it;Install erratum;d130d898-f275-4292-9fd2-1bca8c878caa;john;2018-01-25T14:13:30.000Z;warning;stopped;[u'RHBA-2017:2068, RHEA-2017:1968, RHBA-2017:2171, RHBA-2017:2048, RHBA-2017:1971, RHSA-2017:1868, RHBA-2017:1927, RHBA-2017:2254, RHBA-2017:2118, RHBA-2017:1934, RHBA-2017:2067, RHBA-2017:2167, RHSA-2017:2299, RHSA-2017:1852, RHBA-2017:2083, RHBA-2017:2227, RHBA-2017:1943, RHEA-2017:2280, RHBA-2017:2286, RHEA-2017:2020, RHSA-2017:1793, RHBA-2017:1618, RHBA-2017:1614, RHBA-2017:1306, RHBA-2017:1299, RHEA-2017:1310, RHBA-2017:1317, RHBA-2017:1301, RHBA-2017:0911, RHBA-2017:0928, RHBA-2017:0918, RHSA-2016:2824, RHBA-2017:0092, RHBA-2016:2882, RHSA-2017:0252, RHBA-2017:0400, RHBA-2017:0839, RHBA-2016:2660, RHBA-2017:0103, RHBA-2016:2096, RHBA-2017:0104, RHEA-2016:2832, RHBA-2017:0082, RHBA-2017:0472, RHBA-2017:0377, RHSA-2017:0225, RHBA-2017:0392']
```
```
Job_id;Hostname;Status;Date;Type;User;Errata
182;test.domain.it;succeeded;2017-12-26 16:35:18 UTC;Install Errata - Katello SSH Default;john;RHSA-2017:1793,RHBA-2017:1752,RHSA-2017:1680,RHBA-2017:1674,RHBA-2017:1618,RHBA-2017:1611,RHBA-2017:1614,RHBA-2017:1604,RHBA-2017:1613,RHBA-2017:1605,RHBA-2017:1617,RHSA-2017:1615,RHBA-2017:1607,RHSA-2017:1574,RHSA-2017:1481,RHSA-2017:1484,RHSA-2017:1262,RHBA-2017:1436,RHEA-2017:1437,RHSA-2017:1365,RHSA-2017:1382,RHBA-2017:1306,RHBA-2017:1299,RHEA-2017:1310,RHEA-2017:1307,RHBA-2017:1317,RHBA-2017:1314,RHBA-2017:1302,RHSA-2017:1308,RHBA-
```
