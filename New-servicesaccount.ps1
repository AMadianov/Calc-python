Import-Module activedirectory
cls
$DC='devsps2013.dev.corp'  #-- Контроллер домена для выполнения
$OU='OU=Services,DC=dev,DC=corp'  #-- OU где создаем пользователя
$Logon='sps_webapp_pool'  #-- Указываем логин пользователя
$Description='webapp pool account for SharePoint Farm' <#-- Указать описание, если нужно  #>
$Pass=(Read-Host -AsSecureString "AccountPassword")
    New-ADUser -Name $Logon `
        -DisplayName $Logon `
        -SamAccountName $Logon `
        -AccountPassword $Pass `
        -Path $OU `
        -Description $Description `
        -Company 'Corp ltd.' `
        -CannotChangePassword:$true `
        -PasswordNeverExpires:$true `
        -Server $DC
Enable-ADAccount -Identity $Logon -Server $DC