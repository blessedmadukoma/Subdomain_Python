<?php

class Script 
{
   public $subdomain=[];

   private function JsonDecode(){
        $files=file_get_contents("php_file.json");
        $subdomainsArray=json_decode($files, true);
        return $subdomainsArray;
   }
   public function subdomainArr(){
       $arr=$this->JsonDecode();
    //    print_r($arr);
       foreach($arr as $array){
           $split=explode('//',$array);
            $url=end($split);
            $first=explode('.',$url);
            $subdomainName=$first[0];
            $domain['name']=$subdomainName;
            $domain['url']=$array;
            array_push($this->subdomain, $domain);
       }

       return $this->subdomain;
   }
}





?>