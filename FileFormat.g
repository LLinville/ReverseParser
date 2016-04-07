text outside braces is ignored

braces to open the definition of a token go on their own line

Special tokens include <newline> <space> and <number #-#>
{
    //whitespace before lines is ignored
    //two slashes start a comment

    //the first non-commented line is the name of the token in angle brackets
    <start>
    //the following lines define the forms <start> can take
    //tokens go in <angle_brackets> and have no spaces
    //literals are left on their own
    //definitions end in a semicolon on its own
    i <verb> ;

    //a weight can be assigned after the ending semicolon
    the <noun> <verb_s> ; 3

    //when no weight is added, it takes average weight of all definitions (as if undefined weights start as 1)
    the <noun> <verb_s> <adverb> ;

    //the weight can be one
    a <noun> <verb_s> ; 1

    //the token definition ends with this brace
}

Inter-token text can go here

{
    <noun>
    dog ;
    cat ;
    airplane ;

    //definitions can be recursive
    <adjective_list> <noun> ;
}

Definition blocks can occur in any order

{
    <verb>
    run ; 2
    sprint ; 1
    nap ; 5
}

{
    <verb_s>
    runs ;
    jumps ;
}

{
    <adverb>
    quickly ;
    slowly ;
    high ;
}

{
    <adjective>
    slow ;
    quick ;
    yellow ;
}

{
    <adjective_list>
    <adjective> ;

    //left or right recursion may be used
    <adjective> , <adjective_list> ;
}