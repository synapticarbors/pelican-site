BOOTSTRAP_LESS = custom.less
BOOTSTRAP_RESPONSIVE_LESS = bootstrap/less/responsive.less
OUTPUT_DIR = swatch

swatch:
	recess --compile ${BOOTSTRAP_LESS} > ${OUTPUT_DIR}/bootstrap.css
	recess --compress ${BOOTSTRAP_LESS} > ${OUTPUT_DIR}/bootstrap.min.css
	recess --compile ${BOOTSTRAP_RESPONSIVE_LESS} > ${OUTPUT_DIR}/bootstrap-responsive.css
	recess --compress ${BOOTSTRAP_RESPONSIVE_LESS} > ${OUTPUT_DIR}/bootstrap-responsive.min.css

.PHONY: swatch 
