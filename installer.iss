; Script do Inno Setup para Google Play Reviews Scraper
; Cria um instalador profissional para Windows

#define MyAppName "Google Play Reviews Scraper"
#define MyAppVersion "1.0.0"
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
; SetupIconFile=assets\icons\google-play.ico
Compression=lzma2/max
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
ArchitecturesInstallIn64BitMode=x64

; Configurações visuais (comentado - usar padrão)
; WizardImageFile=compiler:WizModernImage-IS.bmp
; WizardSmallImageFile=compiler:WizModernSmallImage-IS.bmp

[Languages]
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 6.1; Check: not IsAdminInstallMode

[Files]
; Executável principal
Source: "release\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion

; Assets (ícones e bandeiras) - IMPORTANTE!
Source: "assets\*"; DestDir: "{app}\assets"; Flags: ignoreversion recursesubdirs createallsubdirs

; Documentação
Source: "release\LEIA-ME.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "release\LICENSE"; DestDir: "{app}"; Flags: ignoreversion
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "docs\build\TROUBLESHOOTING.md"; DestDir: "{app}"; Flags: ignoreversion isreadme

[Icons]
; Atalho no Menu Iniciar
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:ProgramOnTheWeb,{#MyAppName}}"; Filename: "{#MyAppURL}"
Name: "{group}\Leia-me"; Filename: "{app}\LEIA-ME.txt"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
; Atalho na Área de Trabalho
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
; Atalho na Barra de Inicialização Rápida
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

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

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    // Mensagem de sucesso
    MsgBox('Instalação concluída com sucesso!' + #13#10 + #13#10 + 
           'O Google Play Reviews Scraper está pronto para uso.' + #13#10 + 
           'Não é necessário instalar Python ou outras dependências.', 
           mbInformation, MB_OK);
  end;
end;
