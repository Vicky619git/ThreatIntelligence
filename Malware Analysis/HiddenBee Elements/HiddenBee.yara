rule HiddenBeeElement
{
    meta:
        author = "Vigneswaran"
	creationdate = "26.08.2021"
	description = "Sample rule written for 2018-08-Hidden-Bee-Elements"
	

    strings:

	$a = "ntdll.dll" nocase ascii wide fullword
	$b = "kernel32.dll" nocase ascii wide fullword
	$c = "advapi32.dll" nocase ascii wide fullword
	$d = "cabinet.dll" nocase ascii wide fullword
	$e = "msvcrt.dll" nocase ascii wide fullword
	$f = "ws2_32.dll" nocase ascii wide fullword
	$g = "iphlpapi.dll" nocase ascii wide fullword
    
    condition:
    	
	4 of ($*) // any 4 of the provided strings
	
}