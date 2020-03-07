#Add-PSSnapin Microsoft.SharePoint.PowerShell

## Settings you may want to change ##
$DatabaseServerName = "SPSSQL"
$DatabaseName = "State_Service"
$stateSAName = "State Service"

New-SPStateServiceDatabase -Name $DatabaseName -DatabaseServer $DatabaseServerName | New-SPStateServiceApplication -Name $stateSAName | New-SPStateServiceApplicationProxy -Name ($stateSAName+" Proxy") -DefaultProxyGroup > $null