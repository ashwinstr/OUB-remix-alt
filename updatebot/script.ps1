#update script of userbot by AshSTR


$repo="C:\Users\ashwi\Documents\GitHub\oub-remix-alt"

Write-Host "You're running the OUB-remix update script."
Write-Host " "

#get username of user
$userName = Read-Host "Enter your github username: "
Write-Host " "

#check whether forked properly or not
$fork = Read-Host "Have you forked oub-remix from sahyam2019 or has the same repo name i.e. oub-remix? [y/n]: "
Write-Host " "

if ($fork -eq 'y')
	{
	git clone https://github.com/${userName}/${repo}.git
	}
elseif ($fork -eq 'n')
	{
	$repo = Read-Host "Enter your repo name: "
	git clone https://github.com/${userName}/${repo}.git
	}
else
	{
        Write-Host " "
        Write-Host "You were only supposed to enter y or n."
        exit 1
	}

Write-Host " "
Write-Host "Updating your oub-remix"
git pull https://github.com/sahyam2019/oub-remix.git
git add .
git commit -m "Windows merge"
git push
Write-Host " "
Write-Host "Updated"