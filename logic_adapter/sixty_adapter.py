from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

text = r"""
                                   .,,*****,.                                   .
                          /###########################*                         
                    .(#####################################(.                   
                .(##############(/,.         ..,/##############/                
             .(###########/.                          ,(##########(             
           /##########*                                   ./#########*          
         (#########,                                        (##########/        
       /########(                                        ,###############*      
      ########(                                        (#########(.#######(     
    *########.     .,(&@@@@@%(,                    ,*##########*    *#######.   
   /#######(   ,@@@@@@@@@@@@@@@@@@%            &@@###########@@@@#   .#######,  
  ,#######/  (@@@@@@@@@@@@@@@@@@@@@@%       .@@&##########%@@@@@@@@&  .#######. 
 .%#######  &@@@@@@@@/      &@@@@@@@@%     ,@##########(   (@@@@@@@@&. .####### 
 /#######. %@@@@@@@@#                     ,##########,      #@@@@@@@@%  /######/
 #######( *@@@@@@@@@. .#&@@@@@&%*       (##########@        .@@@@@@@@@. .%#####(
.#######/ (@@@@@@@@@&@@@@@@@@@@@@@@( ,##########&@@%         @@@@@@@@@/  %######
.#######/ #@@@@@@@@@@@@#//#@@@@@@@@%##########@@@@@%         @@@@@@@@@(  %######
.#######( (@@@@@@@@@&        @@@&##########%@@@@@@@&         @@@@@@@@@* .%######
 ########.*@@@@@@@@@*        *##########( ,@@@@@@@@@        ,@@@@@@@@@. *######(
 /######## %@@@@@@@@/      ,##########/    %@@@@@@@@(       %@@@@@@@@#  #######*
  %#######* &@@@@@@@@#   (##########@@     .&@@@@@@@@%    .&@@@@@@@@&  #######( 
  .########/ /@@@@@@@@&##########%@@#        #@@@@@@@@@@@@@@@@@@@@@#  (#######  
   ,#########  .@@@@###########@@@,            *@@@@@@@@@@@@@@@@@(  .#######%.  
    .#########*  ,##########*.                      .,*///*,.      (########    
      (###################                                       (########/     
       .###############,                                      .##########       
         .###########(.                                    ,###########.        
           .#############/.                            ,(###########(           
              *################/,.              ,*(###############,             
                 .(###########################################(.                
                     .(###################################/.                    
                           ,/#######################/.                          
"""

class SixtyAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        return self.process(statement).confidence

    def process(self, input_statement, additional_response_selection_parameters=None):
        if "60" in input_statement.text:
            statement = Statement(text=text)
            statement.confidence = 1
        else:
            statement = Statement(text="")
            statement.confidence = 0

        return statement