if [ "$#" -ne 1 ]; then    #Almacena el numero de argumentos en la ejecucion y si no hay archivos o si hay mas de un archivo imprime un mensaje.
    echo "You must indicate a filename!"  #
    exit
fi

filename=$1    #Recibe el numero de archivos tomados en la ejecucion

if [ ! -f $filename ]; then    #Pregunta si el archivo existe  o no
    echo "File '" $filename "' not found!"
    exit
fi

show_menu(){     #Menu  de opciones
    echo
    echo "Options:"   #Opciones
    echo " 1) Delete duplicates"
    echo " 2) Record count"
    echo " 3) Column names"
    echo " x) exit"
    echo "Select an option: "
    read opt  #Variable que almacena el numero que un usuario digite
}

show_menu
while [ "$opt" != '' ]    #Arranca ciclo While si la variable opt este diferente de vacia
    do
    if [ "$opt" = '' ]; then    #Hace que el pograma termine de ejcutarse si la variable opt tiene espacios en blanco
      exit;
    else
      case $opt in      #condicion case
        1) echo "Option 1 Picked";
            show_menu;
        ;;
        2) echo "Option 2 Picked";
            show_menu;
        ;;
# --->>>
        3) echo "Columns names:"
            head -n 1 $filename | tr ','  '\n';
            echo ""
            show_menu;
# <<<---
        ;;
        x) exit;
        ;;
        \n) exit;
        ;;
        *)echo "Pick an option from the menu";
            show_menu;
        ;;
      esac  #Cierra el case
    fi    #Cierra la condicion
done   #Cierra el do
