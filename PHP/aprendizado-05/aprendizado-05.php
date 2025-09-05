<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP</title>
</head>
<body>
    <?php
        $valor = $_GET['v'];
        $rq = sqrt($valor);
        echo "A raiz de $valor é igual a ".number_format($rq, 2);
    ?>
    <a href="index.html">Voltar</a>
</body>
</html>