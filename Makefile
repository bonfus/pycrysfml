all:
	cp crysfml/Src/*.f90 src/ && \
	cd src && \
	make clean && \
	sed -i "s/\blambda\b/lambde/Ig" *.f90 && \
	sed -i 's/intent (/intent(/gI' *.f90 && \
	sed -i 's/dimension (/dimension(/gI' *.f90 && \
	patch -p0 < fix_uninitialized.patch && \
	make
