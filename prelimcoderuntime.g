LoadPackage("numericalsgps");
DeltaSetPeriodicityBoundForGeneratorList:=function(gs)
	local s, d, l, i, g, S, Sp;
	s:=NumericalSemigroup("generators",gs);
	d:=Gcd(DeltaSetOfSetOfIntegers(gs));
	#d:=Gcd(List(BettiElementsOfNumericalSemigroup(s),x->Minimum(LengthsOfFactorizationsElementWRTNumericalSemigroup(x,s))));
	l:=Length(gs);
	S:=[];
	Sp:=[];

	if l <= 2 then
		return Product(gs);
	fi;

	for i in [2 .. l-1] do
		g:=Gcd([gs[i]-gs[1],gs[1]-gs[l],gs[l]-gs[i]]);
		S[i]:=CeilingOfRational(-(gs[2]*(gs[1]*d*g + (l-2)*(gs[1]-gs[i])*(gs[1]-gs[l])))/((gs[1]-gs[2])*g));
		Sp[i]:=CeilingOfRational((gs[l-1]*((l-2)*(gs[1]-gs[l])*(gs[l]-gs[i]) - d*gs[l]*g))/((gs[l-1]-gs[l])*g));
	od;
	return Maximum(Union(S,Sp));
end;
DeltaSetUnionUpToElementForGeneratorList:=function(n,gs)
    local s, lengths, delta, m, lens, start, finish;
	
	start := Runtime();
	s:=NumericalSemigroup("generators",gs);
	lengths:=List([1 .. gs[Length(gs)]],x->[]);
	lengths[1]:=[0];
	delta:=[];

	for m in [1 .. n] do
		lens:=Union(List([1 .. Length(gs)],i->List(lengths[Int((m-gs[i]) mod gs[Length(gs)])+1],l->l+1)));
		if Length(lens) > 0 then
			delta:=Union(delta,DeltaSetOfSetOfIntegers(lens));
		fi;
		lengths[Int(m mod gs[Length(gs)])+1]:=lens;
	od;
	finish := Runtime() - start;
	return finish;
end;
DeltaSetOfGeneratingSet := function(gs)
    return
DeltaSetUnionUpToElementForGeneratorList(DeltaSetPeriodicityBoundForGeneratorList(gs)+gs[Length(gs)]-1,gs);
end;



