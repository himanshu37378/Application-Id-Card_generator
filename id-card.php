<?php 



        $notfound = false;
        include 'config.php';
        $html = '';
        if(isset($_POST['search'])){

             $urn = $_POST['urn'];

             $sql = "Select * from cards where urn='$urn' ";

             $result = mysqli_query($conn, $sql);
 
 
             if(mysqli_num_rows($result)>0){
             $html="<div class='card' style='width:350px; padding:0;' >";
     
               $html.="";
                         while($row=mysqli_fetch_assoc($result)){

                            $sno = $row['sno']; 
                            $name = $row["name"];
                            $fname = $row["fname"];
                            $program = $row['program'];
                            $email = $row['email'];
                            $phone = $row['phone'];
                            $address = $row['address'];
                            $crn = $row['crn'];
                            $urn = $row['urn'];
                            $exp_date = $row['exp_date'];
                            $image = $row['image'];
                                            
                    
                    
                             $html.="
                                        <!-- second id card  -->
                                        <div class='container' style='text-align:center; border:2px dotted black;'>
                                              <div class='header'>
                                                
                                              </div>
                                  
                                              <div class='container-2'>
                                                  <div class='box-1'>
                                                  <img src='$image'/>
                                                  </div>
                                                  
                                                  <div class='box-2'>
                                                      <p style='font-size: 1.5vh;'>NAME</p>
                                                      <h2>$name</h2>
                                                  
                                                      <p style='font-size: 1.2vh; margin-top: 5px; '>F.Name</p>
                                                      <h2>$fname</h2>
                                                                                                     
                                                  </div>
                                                  <div class='box-3'>
                                                  <?php
                                                 
                                                
                                              
             
                                             ?>
                                                  </div>

                                              </div>
                                  
                                              <div class='container-3'>
                                                  <div class='info-1'>
                                                      <div class='id'>
                                                          <h4>ID No</h4>
                                                          <p>$sno</p>
                                                      </div>
                                  
                                                      <div class='dob'>
                                                          <h4>Phone</h4>
                                                          <p>$phone</p>
                                                      </div>
                                  
                                                  </div>
                                                  <div class='info-2'>
                                                      <div class='join-date'>
                                                          <h4>CRN</h4>
                                                          <p>$crn</p>
                                                      </div>
                                                      <div class='expire-date'>
                                                          <h4>URN</h4>
                                                          <p>$urn</p>
                                                      </div>
                                                  </div>
                                                  <div class='info-3'>
                                                      <div class='email'>
                                                          <h4>Address</h4>
                                                          <p>$address</p>
                                                      </div>
                                                      
                                                  </div>
                                                  
                                                  <!-- id card end -->
                                        ";
                                        
                           
                         }
     

             }
            
        }

        include "phpqrcode/qrlib.php";

                            $PNG_TEMP_DIR = 'assets/images/';
                            if (!file_exists($PNG_TEMP_DIR))
                               mkdir($PNG_TEMP_DIR);
                            
                            $filename = $PNG_TEMP_DIR . 'test.png';
                            
                            if (isset($_POST["search"])) {
                            
                            $codeString = $name . "\n";
                            $codeString .= $program . "\n";
                            $codeString .= $crn . "\n";
                            $codeString .= $urn . "\n";
                            $codeString .= $phone;
                            
                            $filename = $PNG_TEMP_DIR . 'test' . md5($codeString) . '.png';
                            
                            QRcode::png($codeString, $filename);
                            
                            $link = ' . $PNG_TEMP_DIR . basename($filename) . ';
                            
                            }

?>

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <link rel="icon" type="image/png" href="images/favicon.png"/>
    <link rel="stylesheet" href="css/dashboard.css">
    
    <link rel="icon" type="image/png" href="images/favicon.png"/>

    <title>ID-Card Generation</title>
       <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet">



<link rel = "Stylesheet" href= "style.css">
<style>
    .card-body {
     display: flex;
     align-items: center;
     }
</style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/dom-to-image/2.6.0/dom-to-image.js"></script>
  </head>
  <body>


  <div>
<img src= "assets/images/logo.png" width="100%"/>
</div>
 

  <div class="row align-items-center" style="margin: 50px 150px 150px 150px">
  <div class="col">
      <div class="card">
          <div class="card-header" >
              Here is your Id Card
          </div>
        <div class="card-body align-items-center" id="">
            <div id = "mycard">
          <?php echo $html ;
                echo '<img class = "qr-code" src="' . $PNG_TEMP_DIR . basename($filename) . '" />'; ?>
                </div>
</div>
             

        </div>  
        </div>    
        </div> 

       
<button id="demo" class="downloadtable btn btn-primary" onclick="downloadtable()"> Download Id Card</button>



  </div>


    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>

    <script>

    function downloadtable() {

        var node = document.getElementById('mycard');

        domtoimage.toPng(node)
            .then(function (dataUrl) {
                var img = new Image();
                img.src = dataUrl;
                downloadURI(dataUrl, "staff-id-card.png")
            })
            .catch(function (error) {
                console.error('oops, something went wrong', error);
            });

    }



    function downloadURI(uri, name) {
        var link = document.createElement("a");
        link.download = name;
        link.href = uri;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        delete link;
    }




</script>
  </body>

</html>