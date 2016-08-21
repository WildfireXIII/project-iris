import Intelligence
import time
from termcolor import colored
import os
import gc
import json

# log types
LOG_CACHE = "cache"
LOG_CACHE_DETAIL = "cachedetail"
LOG_CONCEPT_PARSE = "conceptparse"
LOG_INTELLIGENCE = "intelligence"
LOG_SYNTAX = "syntax"
LOG_EXECUTION = "execution"
LOG_TIMING = "timing"
LOG_ERROR = "error"
LOG_PLATFORM = "platform"
LOG_DIALOG = "dialog"

# log colors
LOG_CACHE_COLOR = "red"
LOG_CACHE_DETAIL_COLOR = "white"
LOG_CONCEPT_PARSE_COLOR = "blue"
LOG_INTELLIGENCE_COLOR = "yellow"
LOG_SYNTAX_COLOR = "green"
LOG_EXECUTION_COLOR = "magenta"
LOG_TIMING_COLOR = "cyan"
LOG_ERROR_COLOR = "red"
LOG_PLATFORM_COLOR = "white"
LOG_DIALOG_COLOR = "white"


class IntelligencePlatform:


    # LOG TYPES:
    # cache - status messages about when cache is being accessed
    # cachedetail - prints what's being put into cache 
    # conceptparse - status and results of concept parsing
    # intelligence - strings intelligence is passing to platform
    # syntax - granular information about syntax parsing and what's being executed
    # error - any error messages
    # platform - platform messages

    logCacheOn = True
    logCacheDetailOn = True
    logConceptParseOn = True
    logIntelligenceOn = True
    logSyntaxOn = True
    logExecutionOn = True
    logTimingOn = True
    logErrorOn = True
    logPlatformOn = True
    logDialogOn = True

    entity = None
    entityData = {}
    entityDataFolderPath = ""
    cycle = 0
            
    level = 0
    cache = []
    argNum = []

    timeStack = []

    continueSelf = True

    logFP = None
    platformLogFP = None

    def CreateEntity(self):
        # load current data
        self.Log("Loading entity data...", LOG_PLATFORM)
        entityFP = open("ENTITY.dat", "r")
        self.entityData = json.load(entityFP)
        entityFP.close()

        # increment build
        self.entityData["Build"] = str(1 + int(self.entityData["Build"])) 

        # save updated
        entityFP = open("ENTITY.dat", "w")
        json.dump(self.entityData, entityFP)

        # create new run folder
        self.Log("Building data folder for new entity...", LOG_PLATFORM)
        folderName = str(self.entityData["Name"]) + " " + str(self.entityData["Version"]) + "." + str(self.entityData["Build"]) + " (" + time.strftime("%y.%m.%d-%H.%M.%S") + ")"
        self.entityDataFolderPath = "InstanceLogs/" + folderName
        #os.makedirs("./InstanceLogs/" + folderName)
        os.makedirs("./" + self.entityDataFolderPath)
        self.Log("Created Folder: " + self.entityDataFolderPath) 

        # create platform log
        self.platformLogFP = open(self.entityDataFolderPath + "/_PLATFORMLOG.log", "w")

        self.InitializeIntelligence()
        

    def InitializeIntelligence(self):
        self.Log("Instantiating new intelligence instance in entity...", LOG_PLATFORM)
        self.entity = Intelligence.Intelligence()

        self.Log("----------------------------------------", LOG_PLATFORM)
        self.Log("\t" + str(self.entityData["Name"]) + " " + str(self.entityData["Version"]), LOG_PLATFORM)
        self.Log("\tBuild " + str(self.entityData["Build"]), LOG_PLATFORM)
        self.Log("----------------------------------------\n", LOG_PLATFORM)
        
        #self.Log("Recording initial memory...", LOG_PLATFORM)
        # record initial memory set
        self.DumpMemory(True)

    def StartLife(self):
        self.Log("Starting life...\n", LOG_PLATFORM)
        self.cycle = 0

        while (self.continueSelf):
            self.Log("----- CYCLE " + str(self.cycle) + " -----", LOG_PLATFORM)
            
            # create log file
            self.Log("Creating cycle " + str(self.cycle) + " log file...", LOG_PLATFORM)
            self.logFP = open(self.entityDataFolderPath + "/Cycle_" + str(self.cycle) + ".log", "w")

            self.continueSelf = False # should self sustain (keep itself alive by running itself)
            try: 
                self.Log("Running cycle " + str(self.cycle) + "...\n", LOG_PLATFORM)
                self.RunConceptExecute("[self]")
            except:
                self.Log("\nERROR: Self failed to run properly", LOG_ERROR)
                self.logFP.close()
                self.DumpMemory()
                break
            
            self.Log("\nCycle " + str(self.cycle) + " finished execution", LOG_PLATFORM) 
            self.logFP.close()
            self.logFP = None

            # create a memory dump
            self.DumpMemory()

            # TODO: platform cmd here
            
        self.Log("Entity is no longer self sustaining. Shutting down...", LOG_PLATFORM)
        self.level = -100
        self.entity.Memory = None
        self.entity = None

        self.platformLogFP.close()
    
    def KILL(self):
        self.Log("Safely corrupting and deleting entity...", LOG_PLATFORM)
        self.level = -100
        self.entity.Memory = None
        delattr(IntelligencePlatform, "entity")
        delattr(IntelligencePlatform, "cache")

        self.Log("Activating fail safe kill switch...")
        self.RunConceptGet = self.FAIL_SAFE
        self.RunConceptExecute = self.FAIL_SAFE
        self.CacheStore = self.FAIL_SAFE
        self.CacheRetrieve = self.FAIL_SAFE
        self.CreateEntity = self.FAIL_SAFE
        self.InitializeIntelligence = self.FAIL_SAFE
        self.METAMapConcept = self.FAIL_SAFE
        self.ParseConcepts = self.FAIL_SAFE

        gc.collect();

        self.RunConceptGet()

    def FAIL_SAFE(self):
        self.Log("_FAIL_SAFE_ - KILL SWITCH WAS THROWN. FUNCTION CALL BLOCKED.", LOG_PLATFORM)
        self.Log("_FAIL_SAFE_ - FORCING PROGRAM STOP.", LOG_PLATFORM)
        delattr(IntelligencePlatform, "FAIL_SAFE")
        gc.collect()
        exit()

    def DumpMemory(self, initial = False):
        backupFileName = ""
        if initial:
            self.Log("Backing up initial entity memory set...", LOG_PLATFORM)
            backupFileName = self.entityDataFolderPath + "/_Memory_INITIAL.json"
        else: 
            self.Log("Backing up entity's memory set for cycle " + str(self.cycle) + "...", LOG_PLATFORM)
            backupFileName = self.entityDataFolderPath + "/Memory_" + str(self.cycle) + ".json"

        backupFP = open(backupFileName, "w")
        json.dump(self.entity.Memory, backupFP, indent=4)
        backupFP.close()

        self.Log("Entity memory dumped to " + backupFileName, LOG_PLATFORM)
    

    # get the concepts and arguments from a string   
    def ParseConcepts(self, conceptString, indent = ""):
        indent += "- " 
        self.Log(indent + "Parsing '" + conceptString + "'...", LOG_CONCEPT_PARSE)
        braceLevel = 0
        quoteLevel = 0
        parenLevel = 0
        recordingConcept = True
        conceptNum = 0
        argNum = -1
        concepts = []

        ESCAPE = False

        for character in conceptString:
            if character == "[": braceLevel += 1
            elif character == "]":
                braceLevel -= 1
                if braceLevel == 0:
                    conceptNum += 1
                    recordingConcept = True # if completely finished that part of concept, and potentially starting new one, turn recording back on
                    argNum = -1
            elif character == "(": parenLevel += 1
            elif character == ")": parenLevel -= 1
            elif character == "\\": 
                ESCAPE = True 
                continue
            elif (character == "\"" or character == "'") and not ESCAPE:
                if quoteLevel == 0: quoteLevel += 1
                elif quoteLevel == 1: quoteLevel -= 1
            elif character == " ": recordingConcept = False
            elif recordingConcept:
                try: concepts[conceptNum]
                except IndexError: concepts.append([])
                try: concepts[conceptNum][0]
                except IndexError:
                    concepts[conceptNum].append("") # concept name
                    concepts[conceptNum].append([]) # args
                concepts[conceptNum][0] += character
                
            # argument handling
            if not recordingConcept:
                #print(character + " PAREN LEVEL " + str(parenLevel))
                if character == " " and ((braceLevel == 1 and parenLevel == 0) or (braceLevel == 0 and parenLevel == 1)) and quoteLevel == 0: # space signifies next argument (assuming not in higher level of braces
                    concepts[conceptNum][1].append("")
                    argNum += 1
                else:
                    concepts[conceptNum][1][argNum] += character
                
            if ESCAPE: ESCAPE = False
                
        self.Log(indent + "Parsed " + str(concepts), LOG_CONCEPT_PARSE)
        return concepts 


    def GetLevelIndent(self, level):
        indent = ""
        for i in range(0, level):
            indent += "    "
        return indent

    # gets the part within brackets of the reference
    def GetReferenceName(self, reference):
        conceptStartIndex = reference.find("\"", 0) + 1
        conceptEndIndex = reference.find("\"", conceptStartIndex)

        return reference[conceptStartIndex:conceptEndIndex]

    def RunConceptGet(self, conceptString, multiLevel = False, preConstructedString = ""):
        self.Log("Intelligence:" + conceptString, LOG_INTELLIGENCE)
        indent = self.GetLevelIndent(self.level)
        self.Log(indent + "LEVEL: " + str(self.level), LOG_SYNTAX)

        conceptList = self.ParseConcepts(conceptString, indent)

        reference = ""

        # the thing should be the first
        conceptName = conceptList[0][0]
        if not multiLevel: reference = "self.entity.Memory[\"" + conceptName + "\"]"
        else: reference = "[\"" + conceptName + "\"]"

        if len(conceptList[0][1]) > 0:
            self.Log(indent + "[" + str(self.level) + "](getting argument '" + str(conceptList[0][1]) + "')", LOG_EXECUTION)
            self.level += 1
            self.timeStack.append(time.clock()) # TIMING

            # make sure thing actually exists
            try:
                #self.Log("=============== evaluating '" + str(preConstructedString + reference) + "' ==================") # DEBUG
                eval(preConstructedString + reference)
            except:
                #self.Log("----------------- creating '" + str(preConstructedString + reference) + "' -----------------------") # DEBUG
                exec(preConstructedString + reference + " = {}")
            
            reference += self.RunConceptGet(conceptList[0][1][0], True, str(preConstructedString + reference))
            runTime = (time.clock() - self.timeStack.pop()) * 1000
            self.level -= 1
            
            self.Log(indent + "[" + str(self.level) + "](argument '" + str(conceptList[0][1]) + "' obtained: .......... " + str(runTime) + " ms)", LOG_TIMING)
            
        if not multiLevel: self.CacheStore(reference)
        else: return reference

    def RunConceptExecute(self, conceptString):
        self.Log("Intelligence:" + conceptString, LOG_INTELLIGENCE)
        indent = self.GetLevelIndent(self.level)

        self.Log(indent + "LEVEL: " + str(self.level), LOG_SYNTAX)

        conceptList = self.ParseConcepts(conceptString, indent)

        for concept in conceptList:
            self.Log(indent + "CONCEPT: " + concept[0], LOG_SYNTAX)

            # ensure argnum exists for this level
            while len(self.argNum) <= self.level:
                self.argNum.append(0)
                
            self.argNum[self.level] = 0
            for argument in concept[1]:
                self.Log(indent + "  ARGUMENT: " + str(argument), LOG_SYNTAX)

                # execute argument 
                if argument.startswith("["):
                    self.Log(indent + "[" + str(self.level) + "](executing argument '" + argument + "')", LOG_EXECUTION)
                    self.level += 1
                    self.timeStack.append(time.clock()) # TIMING
                    self.RunConceptExecute(argument)
                    runTime = (time.clock() - self.timeStack.pop()) * 1000
                    self.level -= 1

                    self.Log(indent + "[" + str(self.level) + "](argument '" + argument + "' execution: .......... " + str(runTime) + " ms)", LOG_TIMING)

                # get argument
                if argument.startswith("("):
                    self.Log(indent + "[" + str(self.level) + "](getting argument '" + argument + "')", LOG_EXECUTION)
                    self.level += 1
                    self.timeStack.append(time.clock()) # TIMING
                    self.RunConceptGet(argument)
                    runTime = (time.clock() - self.timeStack.pop()) * 1000
                    self.level -= 1

                    self.Log(indent + "[" + str(self.level) + "](argument '" + argument + "' obtained: .......... " + str(runTime) + " ms)", LOG_TIMING)

                # literal argument (but not for the python!!!)
                if argument.startswith("\"") and concept[0] != "python":
                    self.Log(indent + "[" + str(self.level) + "](storing literal argument " + argument + ")", LOG_EXECUTION)
                    self.CacheStore(argument, 0)

                self.argNum[self.level] += 1

            # execute concept
            if concept[0] == "python":
                code = concept[1][0][1:-1]
                self.Log(indent + "EXECUTING: '" + code + "'", LOG_SYNTAX)
                exec(code)
            else:
                runstring = self.entity.Memory[concept[0]]

                if runstring == "[self]":
                    self.continueSelf = True
                    return
                
                self.Log(indent + "[" + str(self.level) + "](executing concept '" + concept[0] + "')", LOG_EXECUTION)
                self.level += 1
                self.timeStack.append(time.clock()) # TIMING
                self.RunConceptExecute(runstring)
                runTime = (time.clock() - self.timeStack.pop()) * 1000
                self.level -= 1
                self.Log(indent + "[" + str(self.level) + "](concept '" + concept[0] + "' execution: ......... " + str(runTime) + " ms)", LOG_TIMING)
                self.CacheClear()


    # verifies appropriate structures exist in cache, then stores object in cache based on level
    # if for some reason trying to get a different level's cache, specify an offset
    # (by default, since this is generally for arguments, arguments are for the
    # level above it?)
    def CacheStore(self, obj, offset = -1):
        level = self.level + offset

        # ensure structures exist
        while len(self.cache) <= level:
            self.cache.append([])
        while len(self.argNum) <= level:
            self.argNum.append(0)
        while len(self.cache[level]) <= self.argNum[level]:
            self.cache[level].append("")
        
        self.Log("**CACHE**:: STORING at level " + str(level) + " at " + str(self.argNum[level]), LOG_CACHE)
        self.Log("########## STORE ##########\n" + str(obj) + "\n###########################\n", LOG_CACHE_DETAIL)
        self.cache[level][self.argNum[level]] = obj

    def CacheRetrieve(self, argNum, offset = 0):
        level = self.level + offset

        self.Log("**CACHE**:: RETRIEVING at level " + str(level) + " at " + str(argNum), LOG_CACHE)

        obj = None
        try: obj = self.cache[level][argNum]
        except IndexError:
            self.Log("**CACHE**:: RETRIVAL FAILURE", LOG_CACHE)
            return None
        self.Log("########## RETRIEVE ##########\n" + str(obj) + "\n##############################\n", LOG_CACHE_DETAIL)
        return obj

    def CacheClear(self, offset = 0):
        level = self.level + offset

        self.Log("**CACHE**:: CLEARING level " + str(level), LOG_CACHE)
        try: 
            self.cache[level] = []
            self.argNum[level] = 0
        except IndexError:
            self.Log("**CACHE**:: CLEARING FAILURE", LOG_CACHE)

    def GetInput(self):
        inputstr = raw_input('Intelligence requested input: ')
        self.Log("Creator> " + inputstr, LOG_PLATFORM)
        return inputstr

    def Display(self, msg):
        self.Log(str(self.entityData["Name"]) + " " + str(self.entityData["Version"]) + "." + str(self.entityData["Build"]) + "> " + msg, LOG_PLATFORM)
            
    def Log(self, msg, level = "default"):

        if self.logFP != None: self.logFP.write(msg + "\n")
        if self.platformLogFP != None and (level == LOG_PLATFORM or level == LOG_ERROR or level == LOG_DIALOG): self.platformLogFP.write(msg + "\n")
        
        if level == LOG_CACHE and self.logCacheOn: 
            print(colored(str(msg), LOG_CACHE_COLOR))
            return
        elif level == LOG_CACHE_DETAIL and self.logCacheDetailOn:
            print(colored(str(msg), LOG_CACHE_DETAIL_COLOR))
            return
        elif level == LOG_CONCEPT_PARSE and self.logConceptParseOn:
            print(colored(str(msg), LOG_CONCEPT_PARSE_COLOR))
            return
        elif level == LOG_INTELLIGENCE and self.logIntelligenceOn:
            print(colored(str(msg), LOG_INTELLIGENCE_COLOR))
            return
        elif level == LOG_SYNTAX and self.logSyntaxOn:
            print(colored(str(msg), LOG_SYNTAX_COLOR))
            return
        elif level == LOG_EXECUTION and self.logExecutionOn:
            print(colored(str(msg), LOG_EXECUTION_COLOR))
            return
        elif level == LOG_TIMING and self.logTimingOn:
            print(colored(str(msg), LOG_TIMING_COLOR))
            return
        elif level == LOG_ERROR and self.logErrorOn:
            print(colored(str(msg), LOG_ERROR_COLOR))
            return
        elif level == LOG_PLATFORM and self.logPlatformOn:
            print(colored(str(msg), LOG_PLATFORM_COLOR))
            return
        elif level == LOG_DIALOG and self.logDialogOn:
            print(colored(str(msg), LOG_DIALOG_COLOR))
            return
        elif level == "default":
            print(msg)
            return
        else:
            return


    # TODO: logically this should be in the concept itself, but slower?
    # TEMP_ARG_0 is the REFERENCE to the desired concept NOTE: this shouldn't
    # even be used!!!!!!!!!
    # TEMP_MAP_CONCEPT is the VALUE of that concept
    # TEMP_MAP_LOC is the place to store the map
    def METAMapConcept(self):
        mapStorage = self.entity.Memory["TEMP_MAP_LOC"]
        conceptList = self.ParseConcepts(self.entity.Memory["TEMP_MAP_CONCEPT"])
        self.entity.Memory[mapStorage] = {}
        index = -1
        for concept in conceptList:
            index += 1
            indexString = str(index)
            self.entity.Memory[mapStorage][indexString] = {}
            self.entity.Memory[mapStorage][indexString]["concept"] = concept[0]

            # create a straight string of the args TODO: maybe later find a way to make
            # this a recursive structure like it would be anyway?
            argsString = ""
            for argument in concept[1]:
                argsString += " " + str(argument)
            
            self.entity.Memory[mapStorage][indexString]["args"] = argsString