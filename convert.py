import sys
f = open(sys.argv[1])
ls = f.readlines()
f.close()

cvtDict = {
  "Blacks2012" : 0,
  "BlueHue" : 0,
  "BlueSaturation" : 0,
  "CameraProfile" : 0,
  "Clarity2012" : 15,
  "Contrast2012" :11,
  "ConvertToGrayscale" : 0,
  "EnableCalibration" : 0,
  "EnableColorAdjustments" : 0,
  "EnableSplitToning" : 0,
  "GreenHue" : 0,
  "GreenSaturation" : 3,
  "Highlights2012" :5,
  "HueAdjustmentAqua" : 6,
  "HueAdjustmentBlue" :17,
  "HueAdjustmentGreen" :3,
  "HueAdjustmentMagenta" : 16,
  "HueAdjustmentOrange" :20,
  "HueAdjustmentPurple" : 26,
  "HueAdjustmentRed" : 5,
  "HueAdjustmentYellow" : 39,
  "LuminanceAdjustmentAqua" : 0,
  "LuminanceAdjustmentBlue" : 0,
  "LuminanceAdjustmentGreen" : 0,
  "LuminanceAdjustmentMagenta" :9,
  "LuminanceAdjustmentOrange" :3,
  "LuminanceAdjustmentPurple" :6,
  "LuminanceAdjustmentRed" : 0,
  "LuminanceAdjustmentYellow" : 4,
  "ParametricDarks" :7,
  "ParametricHighlightSplit" : 75,
  "ParametricHighlights" :11,
  "ParametricLights" :5,
  "ParametricMidtoneSplit" : 50,
  "ParametricShadowSplit" : 25,
  "ParametricShadows" :12,
  "ProcessVersion" : 7,
  "RedHue" : 0,
  "RedSaturation" : 0,
  "Saturation" : 3,
  "SaturationAdjustmentAqua" : 27,
  "SaturationAdjustmentBlue" : 17,
  "SaturationAdjustmentGreen" : 12,
  "SaturationAdjustmentMagenta" : 1,
  "SaturationAdjustmentOrange" : 27,
  "SaturationAdjustmentPurple" : 10,
  "SaturationAdjustmentRed" : 20,
  "SaturationAdjustmentYellow" :11,
  "ShadowTint" : 0,
  "Shadows2012" : 2,
  "SplitToningBalance" : 0,
  "SplitToningHighlightHue" : 0,
  "SplitToningHighlightSaturation" : 0,
  "SplitToningShadowHue" : 0,
  "SplitToningShadowSaturation" : 0,
  "ToneCurveName2012" : "SillyDuck",
  "Vibrance" : 0,
  "Whites2012" : -3,
  "UUID" : "387B9E28-C2A1-4D31-95CD-8A8154E68611",
  "ToneCurvePV2012" : "",
  "ToneCurvePV2012Blue" : "",
  "ToneCurvePV2012Green" : "",
  "title" : sys.argv[1][:-4]
}

xmlns_crs = ""

specialList = ['ToneCurvePV2012', 'ToneCurvePV2012Blue', 'ToneCurvePV2012Green']

for l in ls:
  for k in cvtDict:
    if "xmlns:crs" in l:
      xmlns_crs = l.split('=')[1][1:-2]
    if k not in specialList and k in l:
      val = l.split('=')[1][1:-2]
      try:
        val = int(val)
      except ValueError:
        if val == 'True':
          val = 'true'
        elif val == 'False':
          val = 'false'
        else:
          val = '"'+val+'"'
      cvtDict[k] = val

import xml.etree.ElementTree as ET
tree = ET.parse(sys.argv[1])
root = tree.getroot()

for i in specialList:
  for child in root.findall('.//{'+xmlns_crs+'}'+i):
    #print(child.tag,child.attrib,child.text)
    strList = []
    for cc in child.iter():
      print(cc.tag,cc.attrib,cc.text)
      if ',' in cc.text:
        strList.append( cc.text.split(',')[0] )
        strList.append( cc.text.split(',')[1][1:] )
    cvtDict[i] = ','.join(strList)


lrt = """s = {{
  id = "674AC6B8-B28A-4A4E-85A5-71DC2738115D",
  internalName = "test internalName",
  title = "{title}",
  type = "Develop",
  value = {{
    settings = {{
      Blacks2012 = {Blacks2012},
      BlueHue = {BlueHue},
      BlueSaturation = {BlueSaturation},
      CameraProfile = {CameraProfile},
      Clarity2012 = {Clarity2012},
      Contrast2012 = {Contrast2012},
      ConvertToGrayscale = {ConvertToGrayscale},
      EnableCalibration = {EnableCalibration},
      EnableColorAdjustments = {EnableColorAdjustments},
      EnableSplitToning = {EnableSplitToning},
      GreenHue = {GreenHue},
      GreenSaturation = {GreenSaturation},
      Highlights2012 = {Highlights2012},
      HueAdjustmentAqua = {HueAdjustmentAqua},
      HueAdjustmentBlue = {HueAdjustmentBlue},
      HueAdjustmentGreen = {HueAdjustmentGreen},
      HueAdjustmentMagenta = {HueAdjustmentMagenta},
      HueAdjustmentOrange = {HueAdjustmentOrange},
      HueAdjustmentPurple = {HueAdjustmentPurple},
      HueAdjustmentRed = {HueAdjustmentRed},
      HueAdjustmentYellow = {HueAdjustmentYellow},
      LuminanceAdjustmentAqua = {LuminanceAdjustmentAqua},
      LuminanceAdjustmentBlue = {LuminanceAdjustmentBlue},
      LuminanceAdjustmentGreen = {LuminanceAdjustmentGreen},
      LuminanceAdjustmentMagenta = {LuminanceAdjustmentMagenta},
      LuminanceAdjustmentOrange = {LuminanceAdjustmentOrange},
      LuminanceAdjustmentPurple = {LuminanceAdjustmentPurple},
      LuminanceAdjustmentRed = {LuminanceAdjustmentRed},
      LuminanceAdjustmentYellow = {LuminanceAdjustmentYellow},
      ParametricDarks = {ParametricDarks},
      ParametricHighlightSplit = {ParametricHighlightSplit},
      ParametricHighlights = {ParametricHighlights},
      ParametricLights = {ParametricLights},
      ParametricMidtoneSplit = {ParametricMidtoneSplit},
      ParametricShadowSplit = {ParametricShadowSplit},
      ParametricShadows = - {ParametricShadows},
      ProcessVersion = {ProcessVersion},
      RedHue = {RedHue},
      RedSaturation = {RedSaturation},
      Saturation = {Saturation},
      SaturationAdjustmentAqua = {SaturationAdjustmentAqua},
      SaturationAdjustmentBlue = {SaturationAdjustmentBlue},
      SaturationAdjustmentGreen = {SaturationAdjustmentGreen},
      SaturationAdjustmentMagenta = {SaturationAdjustmentMagenta},
      SaturationAdjustmentOrange = {SaturationAdjustmentOrange},
      SaturationAdjustmentPurple = {SaturationAdjustmentPurple},
      SaturationAdjustmentRed = {SaturationAdjustmentRed},
      SaturationAdjustmentYellow = {SaturationAdjustmentYellow},
      ShadowTint = {ShadowTint},
      Shadows2012 = {Shadows2012},
      SplitToningBalance = {SplitToningBalance},
      SplitToningHighlightHue = {SplitToningHighlightHue},
      SplitToningHighlightSaturation = {SplitToningHighlightSaturation},
      SplitToningShadowHue = {SplitToningShadowHue},
      SplitToningShadowSaturation = {SplitToningShadowSaturation},
      ToneCurveName2012 = {ToneCurveName2012},
      ToneCurvePV2012 = {{
        {ToneCurvePV2012}
      }},
      ToneCurvePV2012Blue = {{
        {ToneCurvePV2012Blue}
      }},
      ToneCurvePV2012Green = {{
        {ToneCurvePV2012Green}
      }},
      ToneCurvePV2012Red = {{
        0,
        0,
        63,
        63,
        255,
        255,
      }},
      Vibrance = {Vibrance},
      Whites2012 = {Whites2012},
    }},
    uuid = {UUID},
  }},
  version = 0,
}}
""".format(**cvtDict)

f = open(sys.argv[1][:-4]+".lrtemplate","w")
f.write(lrt)
f.close()

#print lrt