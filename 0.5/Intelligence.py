class Intelligence:

    Memory = {
            #"self":"[mutate (self)][query (approval)][remember (self) (approval)][self]",
            #"self":"[print [memory]]",
            #"self":"[print [value (memory)]]",
            #"self":"[print (dictionary (a))]",
            #"self":"[print [value (dictionary (b))]]",
            #"self":"[print [value [test]]]",

            #"self":"[print [run [value [test]]]]",
            #"self":"[print [run [value (memory)]]]]",
            #"self":"[print [value [run [value (memory)]]]]",
            #"self":"[print [value [memory]]]",
            #"self":"[print [value [run [value [test]]]]]",
            #"self":"[print [value (print)]]",
            
            #"self":"[set (THING) \"thing\"][print [value (THING)]]",
            #"self":"[print [value [runvalue (memory)]]]",
            #"self":"[print [runvalue (memory)]]]",
            #"self":"[set (THING (THING1)) \"yes\"][print [value (THING (THING1))]]",
            #"self":"[set (THING (THING1 (THING3))) (self)][print [value (THING (THING1 (THING3)))]]",
            
            #"self":"[print [concept (self)]]",
            #"self":"[print [runnable [concept (self)] [runnable [concept (mutate)]]]]",
            #"self":"[print [runnable [concept (mutate)] [referable [concept (self)]]]]",
            #"self":"[print [runnable \"YEAH\"]]", # TODO: THIS DOESN'T WORK. MAKE THIS WORK.

            #"self":"[print [run [runnable [concept (test)]]]]", # TODO: THIS DOESN'T WORK, (because of extra level), unsure if this SHOULD work or not # NOTE: made it work below, just have to make the runnable include a return concept
            #"self":"[print [run [value [run [value [run [runnable [concept (return)] [referable [concept (test)]]]]]]]]",
            #"self":"[print [run [value [run [value [run [runnable [concept (return)] [referable [concept (test)]]]]]]]]]",


            #"self":"[print [value [run [value [run [value [run [runnable [concept (return)] [referable [concept (test)]]]]]]]]]]", # FREAKING 11 LEVELS DEEP


            #"self":"[set (THING) [quotable [runnable [concept (mutate)] [referable [concept (self)]]]]][print [value (THING)]]", # NOTE: amazing meta powers ACTIVATE!!!!!!!!!!!!!!!
            #"self":"[print [quotable [concept (self)]]]",

            #"self":"[set (INPUT) [quotable [getinput]]][print [value (INPUT)]]",


            #"self":"[set (INPUT) [quotable [getinput]]][set [run [runnable [concept (return)] [referable [value (INPUT)]]]] [quotable [runnable [concept (print)] [referable [concept (Nathan)]]]]][print [value (Nathan)]]",

            #"self":"[print [value (runvalue)]]",
            #"self":"[print [runnable [concept (return)] [referable [concept (levelOne)] [referable [concept (levelTow)]]]]]",

            #"self":"[print [count [count [count [count [count]]]]]]",

            #"self":"[print [test2 \"hello world!\" \"Idk why you say hello, I say goodbye\"]]",

            #"self":"[set (THING1) (self)][set_quoted (THING2) (self)][print [value (THING1)]][print [value (THING2)]]",

            #"self":"[map_concept [concept (self)]][print [value (TEMP_ARG_0)]][print [value (CONCEPT_MAP)]]",
            #"self":"[map_concept [concept (self)]][print [value (TEMP_ARG_0)]]",
            #"self":"[map_concept (runvalue)][print [value (TEMP_ARG_0)]][print [value (TEMP_MAP_CONCEPT)]][print [value (CONCEPT_MAP)]]",
            #"self":"[map_concept (runvalue) (ZECONCEPT)][print [value (ZECONCEPT)]]",
            #"self":"[map_concept (self) (ZECONCEPT)][print [value (ZECONCEPT)]]",


            #"self":"[print [value [run [runnable [concept (return) [referable [concept (self)]]]]]]]",
            #"self":"[print [value [get [referable [concept (self)]]]]]",
            #"self":"[print [get [referable [concept (self)]]]]",
            #"self":"[set_quoted (THING) [concept (self)]][print [value [get [referable [value (THING)]]]]]",
    
            #"self":"[map_concept (self) (SELFMAP)][set_quoted (STORED_GETABLE_0) [reconstruct_map_index_gettable [quotable [count]] (SELFMAP) \"concept\"]][print [value [get [value (STORED_GETABLE_0)]]]]",


            
            #"self":"[map_concept (self) (SELFMAP)][print [reconstruct_map_index [quotable [count]] (SELFMAP)]]", # NOTE: AAWWWWWWWWWWW YEAAAAAAAAAAAAAAHHHHHHHHHH

            #"self":"[if [dequotable \"True\"] [runnable [concept (print)] \"It's true!\"] [runnable [concept (print)] \"It's a dirty lie!\"]]",
            #"self":"[print [concat [dequotable \"hello\"] [dequotable \" world\"]]]", 

            #"self":"[if [= \"5\" \"6\"] [runnable [concept (print)] \"They equal!\"] [runnable [concept (print)] \"They don't equal :(\"]]",

            #"self":"[print [length (dictionary)]]",

            #"self":"[map_concept (self) (SELFMAP)][print [reconstruct (SELFMAP)]]",
            #"self":"[map_concept (map_concept) (SELFMAP)][print [reconstruct (SELFMAP)]]",
            
            #"self":"[map_concept (self) (SELFMAP)][array_shift (SELFMAP) [count [count]]][print [value (SELFMAP)]]",


            "self":"[loop [dequotable \"0\"] [dequotable \"5\"] [runnable [concept (+)] [concat [runnable [concept (argument)]] [concat [dequotable \" \"] [runnable [concept (argument)] [runnable [concept (count)] [runnable [concept (count)]]]]]] [runnable [concept (loopTest)] [runnable [concept (argument)]]]]",
            "loopTest":"[display \"LOOP:\"][display [argument]]",
            
            # TODO: sincerely think about making current set "copy" and set_quoted the actual set? 
            # NOTE: ^ if you think about it, it makes more sense to just have a
            # set_quoted, because you can get the value of a differnet concept
            # if its needed, otherwise, just store string OF THE REFERENCE. Then
            # you get the best of both worlds! (but still like the copy idea)


            # mutate needs:
            #   1. List concepts
            #   2. Choose one randomly
            #   3. Get self string, 
            #   4. Get all base and first level concepts
            #   5. Randomly choose one to modify with the self string


            
            "mutate":"", # theoretically, this needs some kind of way to list all the available concepts.
            "query":"",
            "remember":"",
            "recall":"",

            # BOOLEAN CONCEPTS
            "=":"[python \"self.CacheStore(eval(str(self.CacheRetrieve(0, -1)) + \" == \" + str(self.CacheRetrieve(1, -1))), -2)\"]",
            "<":"[python \"self.CacheStore(eval(str(self.CacheRetrieve(0, -1)) + \" < \" + str(self.CacheRetrieve(1, -1))), -2)\"]",
            ">":"[python \"self.CacheStore(eval(str(self.CacheRetrieve(0, -1)) + \" > \" + str(self.CacheRetrieve(1, -1))), -2)\"]",
            "<=":"[python \"self.CacheStore(eval(str(self.CacheRetrieve(0, -1)) + \" <= \" + str(self.CacheRetrieve(1, -1))), -2)\"]",
            ">=":"[python \"self.CacheStore(eval(str(self.CacheRetrieve(0, -1)) + \" >= \" + str(self.CacheRetrieve(1, -1))), -2)\"]",
            "!=":"[python \"self.CacheStore(eval(str(self.CacheRetrieve(0, -1)) + \" != \" + str(self.CacheRetrieve(1, -1))), -2)\"]",

            # MATH CONCEPTS
            "-":"[python \"self.CacheStore(eval(str(self.CacheRetrieve(0, -1)) + \" - \" + str(self.CacheRetrieve(1, -1))), -2)\"]",
            "+":"[python \"self.CacheStore(eval(str(self.CacheRetrieve(0, -1)) + \" + \" + str(self.CacheRetrieve(1, -1))), -2)\"]",
            "*":"[python \"self.CacheStore(eval(str(self.CacheRetrieve(0, -1)) + \" * \" + str(self.CacheRetrieve(1, -1))), -2)\"]",
            "/":"[python \"self.CacheStore(eval(str(self.CacheRetrieve(0, -1)) + \" / \" + str(self.CacheRetrieve(1, -1))), -2)\"]",

            # CORE CONCEPTS
            "value":"[python \"self.CacheStore(eval(self.CacheRetrieve(0, -1)), -2)\"]",
            "return":"[python \"self.CacheStore(self.CacheRetrieve(0, -1), -3)\"]",
            #"set":"[python \"exec(self.CacheRetrieve(0, -1) + \" = \" + self.CacheRetrieve(1, -1))\"]",
            "set":"[python \"exec(str(self.CacheRetrieve(0, -1)) + \" = \" + str(self.CacheRetrieve(1, -1)))\"]",

            "set_quoted":"[python \"exec(self.CacheRetrieve(0, -1) + \" = '\" + self.CacheRetrieve(1, -1) + \"'\")\"]", # NOTE: this is because if something is passed as an argument, impossible to quote what's there (quotable doesn't work, because argument is a sublevel deep) # TODO: find a better way of doing this!!!

            
            "get":"[python \"self.RunConceptGet(self.CacheRetrieve(0, -1));self.CacheStore(self.CacheRetrieve(1, -1), -2)\"]",

            "run":"[python \"self.RunConceptExecute(self.CacheRetrieve(0, -1))\"]", # runs quoted syntax
            #"print":"[python \"print(self.CacheRetrieve(0, -1))\"]",
            "print":"[python \"self.Display(str(self.CacheRetrieve(0, -1)))\"]",
            #"getinput":"[python \"self.CacheStore(raw_input('Intelligence requested input: '), -2)\"]",
            "getinput":"[python \"self.CacheStore(self.GetInput(), -2)\"]",
            "count":"[python \"if self.CacheRetrieve(0, -1) == None:\n\tself.CacheStore(int(0), -2)\nelse:\n\tself.CacheStore(eval('1+int(self.CacheRetrieve(0, -1))'), -2)\"]", # meta concept to potentially keep!

            "argument":"[python \"if self.CacheRetrieve(0, -1) == None:\n\tself.CacheStore(self.CacheRetrieve(0, -3), -2)\nelse:\n\tself.CacheStore(self.CacheRetrieve(int(self.CacheRetrieve(0, -1)), -3), -2)\"]",


            "concat":"[python \"self.CacheStore(str(self.CacheRetrieve(0, -1)) + str(self.CacheRetrieve(1, -1)), -2)\"]",


            "if":"[python \"if (eval(str(self.CacheRetrieve(0, -1))) == True):self.RunConceptExecute(self.CacheRetrieve(1, -1))\nelif self.CacheRetrieve(2, -1) != None:self.RunConceptExecute(self.CacheRetrieve(2, -1))\"]",

            "length":"[python \"self.CacheStore(len(eval(str(self.CacheRetrieve(0, -1))).keys()), -2)\"]",
            

            # META CORE
            "concept":"[python \"self.CacheStore(self.GetReferenceName(self.CacheRetrieve(0, -1)), -2)\"]", # gets the the name of the concept of a reference

            "runnable":"[python \"if self.CacheRetrieve(1, -1) == None:\n\tself.CacheStore(\\\"[\\\" + self.CacheRetrieve(0, -1) + \\\"]\\\", -2)\nelse:\n\tself.CacheStore(\\\"[\\\" + self.CacheRetrieve(0, -1) + \\\" \\\" + self.CacheRetrieve(1, -1) + \\\"]\\\", -2)\"]",

            #"referable":"[python \"if self.CacheRetrieve(1, -1) == None:\n\tself.CacheStore(\\\"(\\\" + self.CacheRetrieve(0, -1) + \\\")\\\", -2)\nelse:\n\tself.CacheStore(\\\"(\\\" + self.CacheRetrieve(0, -1) + \\\" \\\" + self.CacheRetrieve(1, -1) + \\\")\\\", -2)\"]",
            "referable":"[python \"if self.CacheRetrieve(1, -1) == None:\n\tself.CacheStore(\\\"(\\\" + str(self.CacheRetrieve(0, -1)) + \\\")\\\", -2)\nelse:\n\tself.CacheStore(\\\"(\\\" + str(self.CacheRetrieve(0, -1)) + \\\" \\\" + str(self.CacheRetrieve(1, -1)) + \\\")\\\", -2)\"]",

            #"quotable":"[python \"self.CacheStore(\\\"'\\\" + self.CacheRetrieve(0, -1) + \\\"'\\\", -2)\"]",
            "quotable":"[python \"self.CacheStore(\\\"'\\\" + str(self.CacheRetrieve(0, -1)) + \\\"'\\\", -2)\"]",

            "dequotable":"[python \"self.CacheStore(str(self.CacheRetrieve(0, -1))[1:-1], -2)\"]",

            # META META CORE NOTE: these may have dependencies!
            
            #"map_concept":"[set (TEMP_ARG_0) [argument]][set (TEMP_MAP_CONCEPT) [value [value (TEMP_ARG_0)]]]",
            #"map_concept":"[set (TEMP_ARG_0) [argument]][set (TEMP_MAP_CONCEPT) [quotable [value (TEMP_ARG_0)]]]",
            #"map_concept":"[set_quoted (TEMP_ARG_0) [argument]][set (TEMP_MAP_CONCEPT) [quotable [value (TEMP_ARG_0)]]]",
            "map_concept":"" +
                "[set_quoted (TEMP_ARG_0) [argument]]" +
                "[set (TEMP_MAP_CONCEPT) [value (TEMP_ARG_0)]]" +
                "[set_quoted (TEMP_ARG_1) [argument [count [count]]]]" +
                "[set_quoted (TEMP_MAP_LOC) [concept [value (TEMP_ARG_1)]]]" +
                "[python \"self.METAMapConcept()\"]",

            #"reconstruct":"[

            #"reconstruct_map_index":"" + 
                #"[set (TEMP_RECONSTRUCT_MAP_INDEX) [argument]]" +
                #"[set_quoted (TEMP_RECONSTRUCT_MAP_LOC) [argument [count [count]]]]" +
                #"[set_quoted (STORED_GETABLE_0) [reconstruct_map_index_gettable [value (TEMP_RECONSTRUCT_MAP_INDEX)] [value (TEMP_RECONSTRUCT_MAP_LOC)] \"concept\"]]" + 
                #"[set_quoted (STORED_GETABLE_1) [reconstruct_map_index_gettable [value (TEMP_RECONSTRUCT_MAP_INDEX)] [value (TEMP_RECONSTRUCT_MAP_LOC)] \"args\"]]" + 
                #"[return [runnable [value [get [value (STORED_GETABLE_0)]]] [value [get [value (STORED_GETABLE_1)]]]]]",
#
            "reconstruct_map_index":"" + 
                "[set (TEMP_RECONSTRUCT_MAP_INDEX) [argument]]" +
                "[set_quoted (TEMP_RECONSTRUCT_MAP_LOC) [argument [count [count]]]]" +
                "[set_quoted (STORED_GETABLE_0) [build_array_gettable_additive [value (TEMP_RECONSTRUCT_MAP_LOC)] [value (TEMP_RECONSTRUCT_MAP_INDEX)] \"concept\"]]" + 
                "[set_quoted (STORED_GETABLE_1) [build_array_gettable_additive [value (TEMP_RECONSTRUCT_MAP_LOC)] [value (TEMP_RECONSTRUCT_MAP_INDEX)] \"args\"]]" + 
                "[return [runnable [value [get [value (STORED_GETABLE_0)]]] [value [get [value (STORED_GETABLE_1)]]]]]",

            #"reconstruct_map_index_gettable":"" +
                #"[set (TEMP_RECONSTRUCT_MAP_INDEX) [argument]]" +
                #"[set_quoted (TEMP_RECONSTRUCT_MAP_LOC) [argument [count [count]]]]" +
                #"[set (TEMP_RECONSTRUCT_MAP_ADDITIVE) [argument [count [count [count]]]]]" + 
                #"[return [referable [concept [value (TEMP_RECONSTRUCT_MAP_LOC)]] [referable [value (TEMP_RECONSTRUCT_MAP_INDEX)] [referable [value (TEMP_RECONSTRUCT_MAP_ADDITIVE)]]]]]",

            "reconstruct":"" + 
                "[set (TEMP_RECURSIVE_RECONSTRUCT_INDEX) [count]]" +
                "[set_quoted (TEMP_RECURSIVE_RECONSTRUCT_MAPLOC) [argument]]" + 
                "[set (TEMP_RECURSIVE_RECONSTRUCT_STRING) \"\"]" +
                "[recursive_reconstruct]" +
                "[return [value (TEMP_RECURSIVE_RECONSTRUCT_STRING)]]", #takes args, sets memory data, then just calls recursive construct without any args
            
            "recursive_reconstruct":"[if [< [value (TEMP_RECURSIVE_RECONSTRUCT_INDEX)] [length [value (TEMP_RECURSIVE_RECONSTRUCT_MAPLOC)]]] [runnable [concept (recursive_reconstruct_build)]]]",

            # temp recursive reconstruct index
            # temp recursive reconstruct string
            # temp recursive reconstruct map loc
 
            "recursive_reconstruct_build":"" +
                "[set_quoted (TEMP_RECURSIVE_RECONSTRUCT_STRING) [concat [value (TEMP_RECURSIVE_RECONSTRUCT_STRING)] [reconstruct_map_index [value (TEMP_RECURSIVE_RECONSTRUCT_INDEX)] [value (TEMP_RECURSIVE_RECONSTRUCT_MAPLOC)]]]]" +
                "[set (TEMP_RECURSIVE_RECONSTRUCT_INDEX) [count [value (TEMP_RECURSIVE_RECONSTRUCT_INDEX)]]]" +
                "[recursive_reconstruct]",


            "build_array_gettable_additive":""+
                "[set_quoted (TEMP_BUILD_ARRAY_GETTABLE_LOC) [argument]]"+
                "[set (TEMP_BUILD_ARRAY_GETTABLE_INDEX) [argument [count [count]]]]"+
                "[set (TEMP_BUILD_ARRAY_GETTABLE_ADDITIVE) [argument [count [count [count]]]]]"+
                "[return [referable [concept [value (TEMP_BUILD_ARRAY_GETTABLE_LOC)]] [referable [value (TEMP_BUILD_ARRAY_GETTABLE_INDEX)] [referable [value (TEMP_BUILD_ARRAY_GETTABLE_ADDITIVE)]]]]]",

            "build_array_gettable":""+
                "[set_quoted (TEMP_BUILD_ARRAY_GETTABLE_LOC) [argument]]"+
                "[set (TEMP_BUILD_ARRAY_GETTABLE_INDEX) [argument [count [count]]]]"+
                "[return [referable [concept [value (TEMP_BUILD_ARRAY_GETTABLE_LOC)]] [referable [value (TEMP_BUILD_ARRAY_GETTABLE_INDEX)]]]]",


            "array_shift":""+
                "[set_quoted (TEMP_ARRAY_SHIFT_LOC) [argument]]"+
                "[set (TEMP_ARRAY_SHIFT_INDEX) [argument [count [count]]]]"+
                #"[set (TEMP_ARRAY_SHIFT_INDEX)
                #"[set (TEMP_ARRAY_SHIFT_CURRENT) [- [length [value [value (TEMP_ARRAY_SHIFT_LOC)]]] [dequotable \"1\"]]]"+
                "[set (TEMP_ARRAY_SHIFT_CURRENT) [length [value [value (TEMP_ARRAY_SHIFT_LOC)]]]]"+
                "[recursive_array_shift]",

            "recursive_array_shift":""+
                "[if [>= [value (TEMP_ARRAY_SHIFT_CURRENT)] [value (TEMP_ARRAY_SHIFT_INDEX)]] [runnable [concept (array_shift_function_dispatch)]]]",

            "array_shift_function_dispatch":"[if [= [value (TEMP_ARRAY_SHIFT_CURRENT)] [value (TEMP_ARRAY_SHIFT_INDEX)]] [runnable [concept (array_shift_function_equal)]] [runnable [concept (array_shift_function_normal)]]]",


            "array_shift_function_normal":""+
                "[set [get [build_array_gettable [value (TEMP_ARRAY_SHIFT_LOC)] [value (TEMP_ARRAY_SHIFT_CURRENT)]]] [value [get [build_array_gettable [value (TEMP_ARRAY_SHIFT_LOC)] [- [value (TEMP_ARRAY_SHIFT_CURRENT)] [dequotable \"1\"]]]]]]"+
                "[set (TEMP_ARRAY_SHIFT_CURRENT) [- [value (TEMP_ARRAY_SHIFT_CURRENT)] [dequotable \"1\"]]]"+
                "[recursive_array_shift]",

            "array_shift_function_equal":""+
                "[set [get [build_array_gettable [value (TEMP_ARRAY_SHIFT_LOC)] [value (TEMP_ARRAY_SHIFT_CURRENT)]]] \"\"]"+
                "[set (TEMP_ARRAY_SHIFT_CURRENT) [- [value (TEMP_ARRAY_SHIFT_CURRENT)] [dequotable \"1\"]]]"+
                "[recursive_array_shift]",





            # NOTE: there's going to have to be a way to "name" a loop and have
            # that be part of all the temporary storages, otherwise nested loops
            # will just overwrite eachother
            # arguments to pass in:
            # 0 - number to start at
            # 1 - number to end at
            # 2 - operation for number (should be REFERENCE to concept of operation?)
            # 3 - function to run
            "loop":""+
                "[set (TEMP_LOOP_INDEX) [argument]]"+
                "[set (TEMP_LOOP_END) [argument [count [count]]]]"+
                "[set_quoted (TEMP_LOOP_OPERATION) [argument [count [count [count]]]]]"+
                "[set_quoted (TEMP_LOOP_RUN) [argument [count [count [count [count]]]]]]",
            

            # future concepts:
            # break concept (stops current concept)


            # concept map testing 
            "connection":"",
            "depth":"[python \"self.CacheStore(self.level - 1, -2)\"]", # this returns the level of the CONCEPT THAT CALLED IT
            
            # TESTING CONCEPTS

            "runvalue":"[set (TEMP) [argument]][return [run [value (TEMP)]]]",
            "printsafe":"[python \"print(\\\"Hello world!\\\")\"]",


            "approval":"0",
            "dictionary":{
                "a":"hello world!!!!",
                "b":"I'M ANOTHER THING!!"
                },
            "memory":"[return (print)]",
            "test":"[return (memory)]",

            "test2":"[set (TEMP) [argument [count [count]]]][return [quotable [value (TEMP)]]]"




            # OLD CONCEPTS

            #"runnable":"[python \"self.CacheStore(\\\"[\\\" + self.CacheRetrieve(0, -1) + \\\"]\\\", -2)\"]", # TODO: need to expand this to be able to construct arguments as well (2nd argument could be the argument string, so we get the same functional structyure thing
            #"argument":"[python \"self.CacheStore(self.CacheRetrieve(0, -3), -2)\"]",
            #"memory":"[python \"self.CacheStore(self.entity.Memory, -2)\"]",

            
            }



    def TestReferences(self):
        x = { "thing":13 }
        print(x) # {'thing':13}
        print(str(x["thing"])) # 13
        reference = "x[\"thing\"]"
        print(reference) # 'x["thing"]'
        print(eval(reference)) # 13
        exec(reference + " = 14")
        print(eval(reference)) # 14
        




# arg0: the name of the concept to map
#
#
# [set (TEMP_ARG_0) [argument]][set (TEMP_MAP_CONCEPT) [value (TEMP_ARG_0)]]
#def METAMapConcept(self):
#   conceptList = self.ParseConcepts(self.entity.Memory["TEMP_MAP_CONCEPT"])
#   self.entity.Memory["CONCEPT_MAP"] = {}
#   index = 0
#   for concept in conceptList:
#       indexString = str(index)
#       self.entity.Memory["CONCEPT_MAP"][indexString] = {}
#       self.entity.Memory["CONCEPT_MAP"][indexString]["concept"] = self.entity.Memory["TEMP_ARG_0"] # the argument, which should be the name of the concept

#       # create a straight string of the args TODO: maybe later find a way to make
#       # this a recursive structure like it would be anyway?
#       argsString = ""
#       for argument in concept[1]:
#           argsString += " " + str(argument)
#       
#       self.entity.Memory["CONCEPT_MAP"][indexString]["args"] = argsString

