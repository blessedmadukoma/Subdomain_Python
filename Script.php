<?php

class Script 
{
   public $subdomain=[];
   public $domain;
   public $error;

   public function __construct($data) {
      $this->domain = $data;
   }

   private function runsrap($domain){
      $run=shell_exec('python c:/wamp64/www/hg/Subdomain_Python/subdomain_lookup.py '. $domain.' 2>&1');
      // echo $run;
      if ($run) {
         return true;
      }else{
         return false;
      }
   }
   private function JsonDecode(){
      $runstatus=$this->runsrap($this->domain);
      if ($runstatus==true) {
         $files=file_get_contents("subdomain_list.json");
         $subdomainsArray=json_decode($files, true);
         return $subdomainsArray;
      }
        
   }
   public function subdomainArr(){
       $arr=$this->JsonDecode();
   // print_r($arr);
      if (!empty($arr)) {
         foreach($arr as $array){
            if (!empty($array)) {
               $split=explode('//',$array);
               $url=end($split);
               $first=explode('.',$url);
               // print_r($first);
               if ($first[0]=='www') {
                  $subdomainName=$first[1];
               }else{
                  $subdomainName=$first[0];
               }
               $domain['name']=$subdomainName;
               $domain['url']=$array;
               array_push($this->subdomain, $domain);
            }
         }
         return $this->subdomain;
      }else{
         $this->error="something went wrong";
         return $this->error;
      }

       
   }
}





?>