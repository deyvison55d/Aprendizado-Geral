<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aprendizado-01</title>
</head>
<body>
    <div>
        <?php
            $n1 = $_GET['a'];
            $n2 = $_GET['b'];
            echo "<h2>Valores recebidos: $n1 e $n2</h2>";
            $media = ($n1 + $n2) / 2;
            echo "A soma vale ". ($n1+$n2);
            echo "<br>A subtração vale ". ($n1 - $n2);
            echo "<br>A multiplicação vale ". ($n1 * $n2);
            echo "<br>A divisão vale ". ($n1 / $n2);
            echo "<br>A média de $n1 e $n2 é ". ($media);
        ?>
    </div>
</body>
</html>