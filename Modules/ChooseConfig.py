import os
import shutil
import time
import json
import pygetwindow

from Core.GUI import *

from Core.Getters import *

from Modules.Root import root


ItemsSquare = 32

RingPositions = [0, 0, 0, 0]
AmuletPositions = [0, 0, 0, 0]


class Errno(Exception):
    pass


'''
    Windows Are Now Created From GUI.py On 'Core' Folder,
    
    Take A Look Around...
'''


class ChooseConfig:
    def __init__(self, CharName):
        self.ChooseConfig = GUI('ChooseConfig', 'Choose You Config')
        self.ChooseConfig.MainWindow('Config', [414, 202], [2, 2.36])

        '''
            This Is The Main Function If The ChooseConfig...
            
            He Is Called When The Player Click On 'Load' Or 'Create' Button.
        '''

        def CreateDefaultJson():
            ScriptToLoad = NameCreateJson.get()

            '''
                When This Function Is Called, He Take A Name From EntryBox, 
                To Do Some Checks In The File.
                
                If The File Already Exist, He Just Throw You For Root Window
                Because You Already Configure Your File.
                
                Else He Create One File With The Name Getted And Starts The Configuration
            '''

            if os.path.isfile('Scripts/' + ScriptToLoad + '.json'):
                with open('Scripts/' + ScriptToLoad + '.json', 'r') as LoadsJson:
                    data = json.load(LoadsJson)

                time.sleep(.5)

                print('')
                print('Your Configure Stats:', data['Stats'])

                if data['MouseOption'] != MouseMode.get():
                    data['MouseOption'] = MouseMode.get()
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                pyautogui.PAUSE = 0.005

                if data['Stats']:
                    print("\nOpening TibiaAuto...")
                    self.ChooseConfig.destroyWindow()
                    time.sleep(0.1)
                    root(CharName, ScriptToLoad)
                else:
                    os.remove('Scripts/' + ScriptToLoad + '.json')
                    CreateDefaultJson()
            else:

                '''
                    Here, He Copy The Base To Default Configuration,
                    
                    After The Copy, He Starts The Search For Configurations,
                    You Can See The Progress On Console,
                    If You Dont Have Any Error, It Takes, Usually Around 4 or 5 seconds
                    For Complete The Configuration
                    
                    I recommended You, If You Dont Have Any Errors In The Configuration,
                    Save Your Configuration File In Other Folder, Because If You
                    Download Another Actualization In The Github, You Can Throw The 
                    Files, To Not Have Configure Again.
                '''

                print('Coping Default Json')
                start_configuration = time.time()
                Directory = os.getcwd()

                shutil.copyfile(Directory + '\\Scripts' + '\\Json.json', os.path.join(Directory + '\\Scripts' + '\\' + NameCreateJson.get() + '.json'))

                TibiaAuto = pygetwindow.getWindowsWithTitle("Choose You Config")[0]
                TibiaAuto.minimize()

                pyautogui.PAUSE = 0.005

                time.sleep(.8)

                with open('Scripts/' + ScriptToLoad + '.json', 'r') as LoadedJson:
                    data = json.load(LoadedJson)

                time.sleep(.5)
                time.sleep(.5)

                try:
                    HealthLocation = GetHealthPosition()
                    print('')
                    print(f"Health Location [X: {HealthLocation[0]} Y: {HealthLocation[1]}]")
                    data['Positions']['LifePosition'][0]['x'] = HealthLocation[0]
                    data['Positions']['LifePosition'][0]['y'] = HealthLocation[1]
                    data['Positions']['LifePosition'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('Helth Position Error')
                    data['Positions']['LifePosition'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                try:
                    ManaLocation = GetManaPosition()
                    print('')
                    print(f"Mana Location [X: {ManaLocation[0]} Y: {ManaLocation[1]}]")
                    print('')
                    data['Positions']['ManaPosition'][0]['x'] = ManaLocation[0]
                    data['Positions']['ManaPosition'][0]['y'] = ManaLocation[1]
                    data['Positions']['ManaPosition'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('Mana Position Error')
                    data['Positions']['ManaPosition'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                try:
                    BattlePositions[0], BattlePositions[1], BattlePositions[2], BattlePositions[3] = GetBattlePosition()
                    print(f"Battle Location [X: {BattlePositions[0]} Y: {BattlePositions[1]}]")
                    data['Positions']['BattlePosition'][0]['x'] = BattlePositions[0]
                    data['Positions']['BattlePosition'][0]['y'] = BattlePositions[1]
                    data['Positions']['BattlePosition'][0]['Stats'] = True
                    time.sleep(.4)
                    data['Boxes']['BattleBox'][0]['x'] = int(BattlePositions[0])
                    data['Boxes']['BattleBox'][0]['y'] = int(BattlePositions[1])
                    data['Boxes']['BattleBox'][0]['w'] = int(BattlePositions[2])
                    data['Boxes']['BattleBox'][0]['h'] = int(BattlePositions[3])
                    data['Boxes']['BattleBox'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('Battle Position Error')
                    data['Positions']['BattlePosition'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                try:
                    StatsPositions[0], StatsPositions[1], StatsPositions[2], StatsPositions[3] = GetStatsPosition()
                    print('')
                    print(f"Status Bar Start [X: {StatsPositions[0]}, Y: {StatsPositions[1]}]")
                    print(f"Status Bar End [X: {StatsPositions[2]}, Y: {StatsPositions[3]}]")
                    print('')
                    time.sleep(.2)
                    data['Boxes']['StatusBarBox'][0]['x'] = int(StatsPositions[0])
                    data['Boxes']['StatusBarBox'][0]['y'] = int(StatsPositions[1])
                    data['Boxes']['StatusBarBox'][0]['w'] = int(StatsPositions[2])
                    data['Boxes']['StatusBarBox'][0]['h'] = int(StatsPositions[3])
                    data['Boxes']['StatusBarBox'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('Status Bar Error')
                    data['Boxes']['StatusBarBox'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                try:
                    RingPositions[0], RingPositions[1] = StatsPositions[0], StatsPositions[1] - 58
                    RingPositions[2] = RingPositions[0] + ItemsSquare - 1
                    RingPositions[3] = RingPositions[1] + ItemsSquare - 1
                    print(f"Ring's Square Start [X: {RingPositions[0]}, Y: {RingPositions[1]}]")
                    print(f"Ring's Square End [X: {RingPositions[2]}, Y: {RingPositions[3]}]")
                    print('')
                    time.sleep(.2)
                    data['Boxes']['RingBox'][0]['x'] = int(RingPositions[0])
                    data['Boxes']['RingBox'][0]['y'] = int(RingPositions[1])
                    data['Boxes']['RingBox'][0]['w'] = int(RingPositions[2])
                    data['Boxes']['RingBox'][0]['h'] = int(RingPositions[3])
                    data['Boxes']['RingBox'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('RingPosition Error')
                    data['Boxes']['RingBox'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                try:
                    AmuletPositions[0], AmuletPositions[1] = StatsPositions[0], StatsPositions[1] - 130
                    AmuletPositions[2] = AmuletPositions[0] + ItemsSquare - 1
                    AmuletPositions[3] = AmuletPositions[1] + ItemsSquare - 1
                    print(f"Amulet's Square Start [X: {AmuletPositions[0]}, Y: {AmuletPositions[1]}]")
                    print(f"Amulet's Square End [X: {AmuletPositions[2]}, Y: {AmuletPositions[3]}]")
                    print('')
                    time.sleep(.2)
                    data['Boxes']['AmuletBox'][0]['x'] = int(AmuletPositions[0])
                    data['Boxes']['AmuletBox'][0]['y'] = int(AmuletPositions[1])
                    data['Boxes']['AmuletBox'][0]['w'] = int(AmuletPositions[2])
                    data['Boxes']['AmuletBox'][0]['h'] = int(AmuletPositions[3])
                    data['Boxes']['AmuletBox'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('AmuletPosition Error')
                    data['Boxes']['AmuletBox'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                try:
                    MapPositions[0], MapPositions[1], MapPositions[2], MapPositions[3] = GetMapPosition()
                    time.sleep(.2)
                    data['Boxes']['MapBox'][0]['x'] = int(MapPositions[0])
                    data['Boxes']['MapBox'][0]['y'] = int(MapPositions[1])
                    data['Boxes']['MapBox'][0]['w'] = int(MapPositions[2])
                    data['Boxes']['MapBox'][0]['h'] = int(MapPositions[3])
                    data['Boxes']['MapBox'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('MapPosition Error')
                    data['Boxes']['MapBox'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                try:
                    Player[0], Player[1], GameWindow[0], GameWindow[1], GameWindow[2], GameWindow[
                        3] = GetPlayerPosition()
                    print('')
                    print(f"Player Position [X: {Player[0]}, Y: {Player[1]}]")
                    print('')
                    print(f"Game Window Start [X: {GameWindow[0]}, Y: {GameWindow[1]}]")
                    print(f"Game Window End [X: {GameWindow[2]}, Y: {GameWindow[3]}]")
                    print('')
                    time.sleep(.2)
                    data['Positions']['PlayerPosition'][0]['x'] = Player[0]
                    data['Positions']['PlayerPosition'][0]['y'] = Player[1]
                    data['Positions']['PlayerPosition'][0]['Stats'] = True
                    data['Boxes']['GameWindowBox'][0]['x'] = int(GameWindow[0])
                    data['Boxes']['GameWindowBox'][0]['y'] = int(GameWindow[1])
                    data['Boxes']['GameWindowBox'][0]['w'] = int(GameWindow[2])
                    data['Boxes']['GameWindowBox'][0]['h'] = int(GameWindow[3])
                    data['Boxes']['GameWindowBox'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('Player Position Error')
                    data['Positions']['PlayerPosition'][0]['Stats'] = False
                    data['Boxes']['GameWindowBox'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                    pass

                try:
                    SQMs[0], SQMs[1], SQMs[2], SQMs[3], SQMs[4], SQMs[5], SQMs[6], SQMs[7], SQMs[8], SQMs[9], SQMs[10], SQMs[
                        11], SQMs[12], SQMs[13], SQMs[14], SQMs[15], SQMs[16], SQMs[17] = SetSQMs()
                    time.sleep(0.1)
                    print(f"1° SQM Location [X: {SQMs[0]}, Y: {SQMs[1]}]")
                    print(f"2° SQM Location [X: {SQMs[2]}, Y: {SQMs[3]}]")
                    print(f"3° SQM Location [X: {SQMs[4]}, Y: {SQMs[5]}]")
                    print(f"4° SQM Location [X: {SQMs[6]}, Y: {SQMs[7]}]")
                    print(f"5° SQM Location [X: {SQMs[8]}, Y: {SQMs[9]}]")
                    print(f"6° SQM Location [X: {SQMs[10]}, Y: {SQMs[11]}]")
                    print(f"7° SQM Location [X: {SQMs[12]}, Y: {SQMs[13]}]")
                    print(f"8° SQM Location [X: {SQMs[14]}, Y: {SQMs[15]}]")
                    print(f"9° SQM Location [X: {SQMs[16]}, Y: {SQMs[17]}]")
                    time.sleep(.4)
                    data['SQM']['SQM1'][0]['x'] = int(SQMs[0])
                    data['SQM']['SQM1'][0]['y'] = int(SQMs[1])
                    data['SQM']['SQM1'][0]['Stats'] = True
                    data['SQM']['SQM2'][0]['x'] = int(SQMs[2])
                    data['SQM']['SQM2'][0]['y'] = int(SQMs[3])
                    data['SQM']['SQM2'][0]['Stats'] = True
                    data['SQM']['SQM3'][0]['x'] = int(SQMs[4])
                    data['SQM']['SQM3'][0]['y'] = int(SQMs[5])
                    data['SQM']['SQM3'][0]['Stats'] = True
                    data['SQM']['SQM4'][0]['x'] = int(SQMs[6])
                    data['SQM']['SQM4'][0]['y'] = int(SQMs[7])
                    data['SQM']['SQM4'][0]['Stats'] = True
                    data['SQM']['SQM5'][0]['x'] = int(SQMs[8])
                    data['SQM']['SQM5'][0]['y'] = int(SQMs[9])
                    data['SQM']['SQM5'][0]['Stats'] = True
                    data['SQM']['SQM6'][0]['x'] = int(SQMs[10])
                    data['SQM']['SQM6'][0]['y'] = int(SQMs[11])
                    data['SQM']['SQM6'][0]['Stats'] = True
                    data['SQM']['SQM7'][0]['x'] = int(SQMs[12])
                    data['SQM']['SQM7'][0]['y'] = int(SQMs[13])
                    data['SQM']['SQM7'][0]['Stats'] = True
                    data['SQM']['SQM8'][0]['x'] = int(SQMs[14])
                    data['SQM']['SQM8'][0]['y'] = int(SQMs[15])
                    data['SQM']['SQM8'][0]['Stats'] = True
                    data['SQM']['SQM9'][0]['x'] = int(SQMs[16])
                    data['SQM']['SQM9'][0]['y'] = int(SQMs[17])
                    data['SQM']['SQM9'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('SQMs Error')
                    data['SQM']['SQM1'][0]['Stats'] = False
                    data['SQM']['SQM2'][0]['Stats'] = False
                    data['SQM']['SQM3'][0]['Stats'] = False
                    data['SQM']['SQM4'][0]['Stats'] = False
                    data['SQM']['SQM5'][0]['Stats'] = False
                    data['SQM']['SQM6'][0]['Stats'] = False
                    data['SQM']['SQM7'][0]['Stats'] = False
                    data['SQM']['SQM8'][0]['Stats'] = False
                    data['SQM']['SQM9'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                data['Stats'] = True
                with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                    json.dump(data, wJson, indent=4)

                data['MouseOption'] = MouseMode.get()
                with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                    json.dump(data, wJson, indent=4)

                if CheckAuto.get():
                    with open('Scripts/Loads.json', 'r') as LoaderJson:
                        data2 = json.load(LoaderJson)

                    data2['Auto'] = True
                    data2['ScriptName'] = ScriptToLoad
                    with open('Scripts/Loads.json', 'w') as wwJson:
                        json.dump(data2, wwJson, indent=4)

                end_configuration = time.time() - start_configuration
                print('')
                print(f"Your Setup Time Is: {end_configuration:.2f} Seconds")
                print('')

                print("Opening TibiaAuto...\n")

                time.sleep(.3)
                self.ChooseConfig.destroyWindow()
                time.sleep(.1)
                ScriptToLoad = NameCreateJson.get()

                '''
                    If Dont Have Any Error, He Throw You For The Root Window, In The 'Modules'
                    In the 'Root.py' File.
                '''

                root(CharName, ScriptToLoad)

        # region Valiables

        NameCreateJson = tk.StringVar()
        NameCreateJson.set('NewConfig')
        CheckAuto = tk.BooleanVar()
        CheckAuto.set(True)
        MouseMode = tk.IntVar()
        MouseMode.set(1)
        HookMode = tk.IntVar()
        HookMode.set(1)

        # endregion

        # region Buttons

        if os.path.isfile('Scripts/' + NameCreateJson.get() + '.json'):
            with open('Scripts/' + NameCreateJson.get() + '.json', 'r') as LoadsJson:
                data = json.load(LoadsJson)
            if data['Stats']:
                self.ChooseConfig.addButton('Load', CreateDefaultJson, [75, 23], [310, 166])
            else:
                self.ChooseConfig.addButton('Create', CreateDefaultJson, [75, 23], [310, 166])
        else:
            self.ChooseConfig.addButton('Create', CreateDefaultJson, [75, 23], [310, 166])

        self.ChooseConfig.addEntry([165, 35], NameCreateJson, 28)

        self.ChooseConfig.addLabel('Name Of The Json Conf', [24, 35])

        LabelSelectOP1 = self.ChooseConfig.addLabel('Select Your Mouse And Keyboard Option', [30, 76])
        LabelSelectOP1.configure(bg=rgb((114, 94, 48)), fg='black')

        RadioMouseMoviment = self.ChooseConfig.addRadio('{Global} Movement Mouse On Focused Window', MouseMode, 1, [10, 95])
        RadioMouseMoviment.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                                     selectcolor=rgb((114, 94, 48)))
        RadioSenderMouse = self.ChooseConfig.addRadio("{OTServer} Send Mouse Events To Tibia's Window", MouseMode, 0,
                                                      [10, 114])
        RadioSenderMouse.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                                   selectcolor=rgb((114, 94, 48)))

        LabelSelectOP2 = self.ChooseConfig.addLabel('Select Your Hook Mode', [30, 136])
        LabelSelectOP2.configure(bg=rgb((114, 94, 48)), fg='black')

        RadioHookWindow = self.ChooseConfig.addRadio("{Global} Hook Directly OBS Screen", HookMode, 1, [10, 155])
        RadioHookWindow.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                                  selectcolor=rgb((114, 94, 48)))

        # endregion

        self.ChooseConfig.loop()
