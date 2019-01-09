Param(
    [string]$Month,
    [string]$FileLocation
   ) 
  
  $secpasswd = ConvertTo-SecureString "AzureContainerRegistryKey*****" -AsPlainText -Force
  $mycred = New-Object System.Management.Automation.PSCredential ("ContainerBank", $secpasswd)
  
  $Conn = Get-AutomationConnection -Name AzureRunAsConnection
  Connect-AzureRmAccount -ServicePrincipal -Tenant $Conn.TenantID `
  -ApplicationId $Conn.ApplicationID -CertificateThumbprint $Conn.CertificateThumbprint
  
  # $AzureContext = Select-AzureRmSubscription -SubscriptionId $ServicePrincipalConnection.SubscriptionID
  
  # Working version 1
  # New-AzureRmContainerGroup -ResourceGroupName ACI -Name acr-task -Image containerbank.azurecr.io/helloacrtasks:v1 -IpAddressType Public -RegistryCredential $mycred -Location southeastasia #-AzureRmContext $AzureContext
  
  # $State = (Get-AzureRmContainerGroup -ResourceGroupName ACI -Name acr-task).State
  
  # Write-Output $State
  
  # version 2
  New-AzureRmContainerGroup `
  -ResourceGroupName ACI `
  -Name acr-task `
  -Image containerbank.azurecr.io/pythonaci:v1 `
  -IpAddressType Public `
  -RegistryCredential $mycred `
  -Location southeastasia `
  -RestartPolicy Never `
  -EnvironmentVariable @{"ACCOUNTNAME"="aspreactstorage";"CONTAINERNAME"="2018demo";"SASTOKEN"="AzureBlobStorageSAS*****";"FOLDERNAME"="pythontest/"}
  
  $State = (Get-AzureRmContainerGroup -ResourceGroupName ACI -Name acr-task).State
  
  while($State -ne "Succeeded" -and $State -ne "Failed")
  {
      Start-Sleep -s 60
      $State = (Get-AzureRmContainerGroup -ResourceGroupName ACI -Name acr-task).State
  }
  
  Write-Output $State
  
  if($State -eq "Succeeded") {
      Get-AzureRmContainerGroup -ResourceGroupName ACI -Name acr-task | Get-AzureRmContainerInstanceLog
      }
  
  Remove-AzureRmContainerGroup -ResourceGroupName ACI -Name acr-task
  
  if($State -eq "Failed") {throw "Bad thing happened"}
  
  
  