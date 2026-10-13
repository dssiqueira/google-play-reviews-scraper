; Inno Setup script for Google Play Reviews Scraper
; Build the exe first, then: python build.py --installer

#define MyAppName "Google Play Reviews Scraper"
#define MyAppVersion "2.0.0"
#define MyAppPublisher "Douglas Siqueira"
#define MyAppURL "https://github.com/dssiqueira/google-play-reviews-scraper"
#define MyAppExeName "GooglePlayReviewsScraper.exe"

[Setup]
; Informações do aplicativo
AppId={{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=LICENSE
InfoBeforeFile=INSTALLER-INFO.txt
OutputDir=installer
OutputBaseFilename=GooglePlayReviewsScraper-Setup-v{#MyAppVersion}
SetupIconFile=assets\icons\google-play.ico
UninstallDisplayIcon={app}\{#MyAppExeName}
Compression=lzma2/max
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
ArchitecturesInstallIn64BitMode=x64


[Languages]
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; Single-file build from `python build.py` (assets are bundled inside the exe)
Source: "dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "LICENSE"; DestDir: "{app}"; Flags: ignoreversion
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Atalho no Menu Iniciar
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:ProgramOnTheWeb,{#MyAppName}}"; Filename: "{#MyAppURL}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
; Atalho na Área de Trabalho
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
; Opção para executar após instalação
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[Code]
// Código Pascal para verificações adicionais
function InitializeSetup(): Boolean;
begin
  Result := True;
  // Verifica se Windows 10 ou superior
  if not (GetWindowsVersion >= $0A000000) then
  begin
    MsgBox('Este programa requer Windows 10 ou superior.', mbError, MB_OK);
    Result := False;
  end;
end;

