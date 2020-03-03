#Add-PSSnapin Microsoft.SharePoint.PowerShell -ErrorAction SilentlyContinue

New-SPConfigurationDatabase -DatabaseName "SPS_Config" -DatabaseServer SPSSQL -AdministrationContentDatabaseName "SPS_Admin_Content" -Passphrase (ConvertTo-SecureString "fuckMAN!pass" -AsPlainText -Force) -FarmCredentials (Get-Credential) -SkipRegisterAsDistributedCacheHost