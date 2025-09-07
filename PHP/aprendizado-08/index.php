<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP</title>
</head>
<body>
    <?php
        $a = $_GET['idade'] ?? 1900;
        $i = date('Y') - $a;
        echo "Você nasceu em $a e tera $i anos. <br>";
        if ($i < 16){
            $tipoVoto = 'não vota';
        }
        elseif (($i >= 16 && $i < 18) || ($i > 65)){
            $tipoVoto = 'voto opcional';
        }
        else{
            $tipoVoto = 'voto obrigatório';
        }
        echo "Para essa idade, $tipoVoto";
    ?>
</body>
</html>