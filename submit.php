<?php
$urn = $_POST["urn"];
$password = $_POST["password"];

include 'config.php';


// if($conn->connect_error) {

// die("Failed to connect : ".$conn->connect_error);

// } else {

// $stmt = $conn->prepare("select * from login_credentials where urn = ?");
// $stmt->bind_param("i", $urn);
// $stmt->execute();
// $stmt_result = $stmt->get_result();
// if($stmt_result->num_rows > 0) {
//     $data = $stmt_result->fetch_assoc();
//     if($data["password"] === $password) {
//         echo "<h2>Login Successfully</h2>";
//     } else{
//     echo "<h2>Invalid Email or password</h2>";
//     }

// } else {
// echo "<h2>Invalid Email or password</h2>";
// }
// }

$query = "SELECT * FROM login_credentials WHERE urn = '$urn' AND password = '$password' ";

$result = $conn->query($query);

if($result ->num_rows == 1){
header("Location: index.php");
}
else{
    echo("hello");
}
$conn->close();
?>