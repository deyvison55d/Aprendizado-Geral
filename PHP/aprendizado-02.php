



<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Funções Aritmeticas</title>
    <style>
        h2{
            font-size: 2rem;
            color: #02ce3fff;
            font: Arial;
        }
    </style>
</head>
<body>
    <div>
        <?php
            $v1 = $_GET['x'];
            $v2 = $_GET['y'];
            echo "<h2>Valores recebidos: $v1 e $v2<br>";
            echo "O valor absoluto de $v2 e ". abs($v2);
            echo "<br>O valor de $v1<sup>$v2</sup> e ". pow($v1, $v2);
            echo "<br>A raiz de $v1 é ". sqrt($v1);
            echo "<br>O valor de $v2 arredondado é ". round($v2);
            echo "<br>A parte inteira de $v2 é ". intval($v2);
            echo "<br>O valor de $v1 em moeda é R$". number_format($v1,2);
        ?>
    </div>
</body>
</html>