
;; Function main (main, funcdef_no=13, decl_uid=2008, cgraph_uid=14, symbol_order=14)

main ()
{
  int a;
  int i;
  int D.2016;

  a = 10;
  i = 0;
  goto <D.2013>;
  <D.2012>:
  N.0_1 = N;
  a = a + N.0_1;
  i = i + 1;
  <D.2013>:
  if (i <= 3) goto <D.2012>; else goto <D.2014>;
  <D.2014>:
  D.2016 = a;
  goto <D.2017>;
  D.2016 = 0;
  goto <D.2017>;
  <D.2017>:
  return D.2016;
}


