$uri = 'https://ios-xe-mgmt.cisco.com:443/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1'

# Credentials for DevNet Always-On sandbox
$password = ConvertTo-SecureString 'C1sco12345' -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential ('developer', $password)

# RESTCONF headers
$headers = @{'Accept' = 'application/yang-data+json' }

# Invoke RESTCONF GET
$response = Invoke-RestMethod -Uri $uri `
    -Method Get `
    -Authentication Basic `
    -Credential $Cred `
    -ContentType 'application/yang-data+json' `
    -Headers $headers `
    -SkipCertificateCheck

# Output full JSON
$response | ConvertTo-Json -Depth 5 | Write-Output

# Show interface name
$response.'Cisco-IOS-XE-interfaces-oper:interface'.name

# Check if it's up
if ($response.'Cisco-IOS-XE-interfaces-oper:interface'.'admin-status' -eq 'if-state-up') {
    Write-Host ($response.'Cisco-IOS-XE-interfaces-oper:interface'.name) 'is up'
}
else {
    Write-Host ($response.'Cisco-IOS-XE-interfaces-oper:interface'.name) 'is down'
}
