
;; Function AddTwo (AddTwo, funcdef_no=13, decl_uid=2008, cgraph_uid=14, symbol_order=13)

AddTwo (int a)
{
  int D.2014;

  a = a + 2;
  D.2014 = a;
  goto <D.2015>;
  <D.2015>:
  return D.2014;
}



;; Function main (main, funcdef_no=14, decl_uid=2010, cgraph_uid=15, symbol_order=14)

main ()
{
  int x;
  int D.2016;

  x = 3;
  x = AddTwo (x);
  D.2016 = x;
  goto <D.2017>;
  D.2016 = 0;
  goto <D.2017>;
  <D.2017>:
  return D.2016;
}


